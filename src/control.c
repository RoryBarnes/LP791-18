/**
   @file control.c

   @brief These subroutines deal with control, including I/O, units, and files.

   @author Rory Barnes ([RoryBarnes](https://github.com/RoryBarnes/))

   @date Jan 7 2015

*/

#include "vplanet.h"

void BodyCopyNULL(BODY *dest,BODY *src,int foo,int iNumBodies,int iBody) {
  // Nothing
}


/*
 * SORTING FUNCTIONS
 */

 //! Case-insensitive `strcmp`
 int strcicmp(char const *a, char const *b)
 {
     for (;; a++, b++) {
         int d = tolower(*a) - tolower(*b);
         if (d != 0 || !*a)
             return d;
     }
 }

//! Dummy struct used to sort options
typedef struct {
    int index;
    char name[OPTLEN];
} SORTED_OPTIONS;

//! Dummy struct used to sort output
typedef struct {
    int index;
    char name[OUTLEN];
} SORTED_OUTPUT;

//! Comparison function for option names
int compare_option_names(const void *p, const void *q) {
    return strcicmp(((SORTED_OPTIONS*)p)->name, ((SORTED_OPTIONS*)q)->name);
}

//! Comparison function for output names
int compare_output_names(const void *p, const void *q) {
    return strcicmp(((SORTED_OUTPUT*)p)->name, ((SORTED_OUTPUT*)q)->name);
}

//! Sort the OPTIONS struct by name
void sort_options(OPTIONS *options, int sorted[]) {
    int iOpt;

    // Sort the options alphabetically by name
    SORTED_OPTIONS sorted_options[MODULEOPTEND];
    for (iOpt=0;iOpt<MODULEOPTEND;iOpt++) {
        sorted_options[iOpt].index = iOpt;
        strcpy(sorted_options[iOpt].name, options[iOpt].cName);
    }
    qsort(sorted_options, MODULEOPTEND, sizeof(sorted_options[0]), compare_option_names);
    // Copy over to the array of indices
    for (iOpt=0;iOpt<MODULEOPTEND;iOpt++) {
        sorted[iOpt] = sorted_options[iOpt].index;
    }
}

//! Sort the OUTPUT struct by name
void sort_output(OUTPUT *output, int sorted[]) {
    int iOpt;

    // Sort the output alphabetically by name
    SORTED_OUTPUT sorted_output[MODULEOUTEND];
    for (iOpt=0;iOpt<MODULEOUTEND;iOpt++) {
        sorted_output[iOpt].index = iOpt;
        strcpy(sorted_output[iOpt].name, output[iOpt].cName);
    }
    qsort(sorted_output, MODULEOUTEND, sizeof(sorted_output[0]), compare_output_names);
    // Copy over to the array of indices
    for (iOpt=0;iOpt<MODULEOUTEND;iOpt++) {
        sorted[iOpt] = sorted_output[iOpt].index;
    }
}

/*
 * Struct Initialization
 */

void InitializeControl(CONTROL *control,MODULE *module) {
  int iBody,iModule;

  control->bOutputLapl=0; // XXX This should become part of EVOLVE -- RUSSELL

  control->iMassRad = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->fnForceBehavior = malloc(control->Evolve.iNumBodies*sizeof(fnForceBehaviorModule*));
  control->fnForceBehaviorMulti = malloc(control->Evolve.iNumBodies*sizeof(fnForceBehaviorModule*));
  control->iNumMultiForce = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->Halt = malloc(control->Evolve.iNumBodies*sizeof(HALT));

  control->fnPropsAux = malloc(control->Evolve.iNumBodies*sizeof(fnPropsAuxModule*));
  control->fnPropsAuxMulti = malloc(control->Evolve.iNumBodies*sizeof(fnPropsAuxModule*));

  for (iBody=0;iBody<control->Evolve.iNumBodies;iBody++) {
    control->fnForceBehavior[iBody] = malloc(module->iNumModules[iBody]*sizeof(fnForceBehaviorModule));
    control->fnPropsAux[iBody] = malloc(module->iNumModules[iBody]*sizeof(fnPropsAuxModule));

    for (iModule=0;iModule<module->iNumModules[iBody];iModule++) {
      module->fnInitializeControl[iBody][iModule](control,iBody);
      control->fnPropsAux[iBody][iModule] = &PropsAuxNULL;
    }
  }

  // Initialize IO error messages
  control->Io.baRocheMessage = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->Io.baCassiniOneMessage = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->Io.baCassiniTwoMessage = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->Io.baEnterHZMessage = malloc(control->Evolve.iNumBodies*sizeof(int));
  for (iBody=0;iBody<control->Evolve.iNumBodies;iBody++) {
    control->Io.baRocheMessage[iBody] = 0;
    control->Io.baCassiniOneMessage[iBody] = 0;
    control->Io.baCassiniTwoMessage[iBody] = 0;
    control->Io.baEnterHZMessage[iBody] = 0;
  }
  control->Io.bDeltaTimeMessage = 0;
  control->Io.bMutualIncMessage = 0;
  // Initialize this value, too. Probably need a whole new structure for CheckProgress
  control->Io.dMaxMutualInc = 0;
}

/**
  This function performs the following tasks:

  1) Allocates control->Evolve.fnBodyCopy, iNumMultiProps, tmpUpdate, daDeriv,
     and control->iNumMultiProps.
  2) Initializes control->bOrbiters
  3) Initializes control->Evolve.iNumModules

 */
void InitializeControlEvolve(BODY *body,CONTROL *control,MODULE *module,UPDATE *update) {
  int iBody,iModule,iSubStep;

  control->Evolve.fnBodyCopy = malloc(control->Evolve.iNumBodies*sizeof(fnBodyCopyModule*));
  control->Evolve.iNumModules = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->iNumMultiProps = malloc(control->Evolve.iNumBodies*sizeof(int));
  control->Evolve.tmpUpdate = malloc(control->Evolve.iNumBodies*sizeof(UPDATE));

  control->Evolve.tmpBody = malloc(control->Evolve.iNumBodies*sizeof(BODY));
  InitializeBodyModules(&control->Evolve.tmpBody,control->Evolve.iNumBodies);

  for (iBody=0;iBody<control->Evolve.iNumBodies;iBody++) {
      control->Evolve.fnBodyCopy[iBody] = malloc(module->iNumModules[iBody]*sizeof(fnBodyCopyModule));

      for (iModule=0;iModule<module->iNumModules[iBody];iModule++) {
         control->Evolve.fnBodyCopy[iBody][iModule] = &BodyCopyNULL;
      }
  }

  /* Currently this only matters for RK4 integration. This should
     be generalized for any integration method. */
  if (control->Evolve.iOneStep == RUNGEKUTTA) {
    control->Evolve.daDeriv = malloc(4*sizeof(double**));
    for (iSubStep=0;iSubStep<4;iSubStep++) {
      control->Evolve.daDeriv[iSubStep] = malloc(control->Evolve.iNumBodies*sizeof(double*));
    }
  }

  // Default to no orbiting bodies
  control->bOrbiters = 0;

  /* First we must determine all the primary variables. The user may not
     input them, but instead a redundant variable. Yet these need to be
     defined before we can call InitializeUpdate. */

  for (iBody=0;iBody<control->Evolve.iNumBodies;iBody++) {
    /* First pass NumModules from MODULE -> CONTROL->EVOLVE */
    control->Evolve.iNumModules[iBody] = module->iNumModules[iBody];

    // If any body has an orbit related module initialized, we have orbiters!
    if (body[iBody].bEqtide || body[iBody].bDistOrb || body[iBody].bPoise || body[iBody].bAtmEsc ||
        body[iBody].bGalHabit || body[iBody].bSpiNBody) {
      control->bOrbiters = 1;
    }
    // Why does bUsingDistOrb exist? Why can't body[iBody].bDistOrb work?
    if (!body[iBody].bDistOrb) {
      control->Evolve.bUsingDistOrb = 0;
    }

  }
}

/*
 * Help functions
 */

void PrintFileTypes(int iFileType) {
  if (iFileType == 0)
    printf("Primary Only");
  else if (iFileType == 1)
    printf("Body Only");
  else if (iFileType == 2)
    printf("Any");
}

void WriteHelpOption(OPTIONS *options, int bLong) {
  if (memcmp(options->cName,"null",4)) {

    if (bLong == 0) {

      // ** Short help **

      if (options->dNeg != 0) {
        printf("[-]");
      }
      printf("%s (",options->cName);

      // Cast
      if (options->iType == 0)
        printf("Bool");
      else if (options->iType == 1)
        printf("Int");
      else if (options->iType == 2)
        printf("Double");
      else if (options->iType == 3)
        printf("String");
      else if (options->iType >= 4)
        printf("Array");
      printf(") -- %s ",options->cDescr);

      if (options->dNeg != 0)
        printf(" [Negative = %s] ",options->cNeg);

      // allowed modules
      printf("{Modules = ");
      if (options->iModuleBit)
        PrintModuleList(stdout,options->iModuleBit);
      else
        printf("ALL");
      printf("} ");

      // allowed input files
      printf("<Files = ");
      PrintFileTypes(options->iFileType);
      printf("> ");

      // default (always last)
      printf("(Default = %s).\n",options->cDefault);
    } else {
      // ** Long help **
      // Header

      // Properties
      printf("%s\n",options->cName);
      printf("==================  ====================================\n");
      printf("**Type**            ");
      if (options->iType == 0) printf("Bool\n");
      else if (options->iType == 1) printf("Int\n");
      else if (options->iType == 2) printf("Double\n");
      else if (options->iType == 3) printf("String\n");
      else if (options->iType >= 4) printf("Array\n");
      if (options->bNeg == 1)
          printf("**Custom unit**     %s\n", options->cNeg);
      else
          printf("**Custom unit**     \n");
      printf("**Modules**         ");
      if (options->iModuleBit) PrintModuleList(stdout, options->iModuleBit);
      else printf("ALL");
      printf("\n");
      printf("**Files**           ");
      PrintFileTypes(options->iFileType);
      printf("\n");
      printf("**Default value**   %s\n", options->cDefault);
      if (memcmp(options->cValues,"null",4)) {
        printf("**Allowed values**  %s\n", options->cValues);
      }
      printf("**Description**     %s\n", options->cDescr);
      // Long description
      if (memcmp(options->cLongDescr,"null",4)) {
          printf("\n**Overview**\n");
          printf("%s\n",options->cLongDescr);
      }
      printf("==================  ====================================\n\n");
    }
  }
}

void WriteHelpOutput(OUTPUT *output, int bLong) {
  if (memcmp(output->cName,"null",4)) {
    if (bLong == 0) {
      // ** Short help **
      if (output->bNeg == 1)
        printf("[-]");
      printf("%s -- %s.",output->cName,output->cDescr);
      if (output->bNeg == 1)
        printf(" [Negative = %s]",output->cNeg);
      printf("\n");
    } else {
      // ** Long help **

      // Properties
      printf("%s\n",output->cName);
      printf("========================  ====================================\n");
      if (output->bNeg == 1)
        printf("**Custom unit**           %s\n", output->cNeg);
      else
        printf("**Custom unit**     \n");
      printf("**Modules**               ");
      if (output->iModuleBit) {
        PrintModuleList(stdout, output->iModuleBit);
      } else {
        printf("ALL");
      }
      printf("\n");
      printf("**Description**           %s\n", output->cDescr);
      printf("========================  ====================================\n\n");
        // Long description
      if (memcmp(output->cLongDescr,"null",4)) {
        printf("%s\n\n",output->cLongDescr);
      }
    }
  }
}

void HelpOptions(OPTIONS *options, int bLong) {
  int iOpt;

  // Sort the OPTIONS struct
  int sorted[MODULEOPTEND];
  sort_options(options, sorted);

  if (!bLong) {
    printf("Format: [Negative forces units] Name -- Description [Negative unit] {Compatible modules} <Permited files> (Default value)\n\n");
  }
  for (iOpt=0;iOpt<MODULEOPTEND;iOpt++) {
    WriteHelpOption(&options[sorted[iOpt]], bLong);
  }
}

void HelpOutput(OUTPUT *output, int bLong) {
  int iOut;

  // Sort the OUTPUT struct
  int sorted[MODULEOUTEND];
  sort_output(output, sorted);

  for (iOut=0;iOut<MODULEOUTEND;iOut++) {
    WriteHelpOutput(&output[sorted[iOut]], bLong);
  }
}

void Help(OPTIONS *options,OUTPUT *output,char exe[],int bLong) {

  printf("\n\t\tHelp Message for %s\n\t\t", exe);
  char* pch = strchr(exe, '\0');
  int sz = (int)(pch - exe) + 17;
  int i;
  for (i = 0; i < sz; i++) printf("-");
  printf("\n\n");

  printf("Lead Developer: Rory Barnes\n\n");
  printf("\n%s is a general purpose planetary evolution integrator. From the command\n", exe);
  printf(
    "line, enter one optional command line option and one file name, e.g.:\n\n"
    "> vplanet vpl.in\n\n"
    "where vpl.in is the \"primary\" input file consisting of options and a list\n"
    "of files that contain the initial conditions for all bodies in a system.\n"
    "The code then simulates planetary systen evolution forward or backward in\n"
    "time. This onboard help provides information regarding the input and output\n"
    "files, command line options, and each option and output parameter. For more\n"
    "more information, see https://virtualplanetarylaboratory.github.io/vplanet,\n"
    "or consult the examples directory.\n\n"
  );

  printf("Command Line Options\n");
  printf("====================   ==========================================================\n");
  printf("-v, -verbose           -- Maximum verbosity, i.e. display all warnings and updates.\n");
  printf("-q, -quiet             -- No verbosity, i.e. nothing printed to device.\n");
  printf("-h, -help              -- Display short help.\n");
  printf("-H, -Help              -- Display extended help.\n");
  printf("====================   ==========================================================\n\n");

  printf("Input File Structure\n");
  printf("====================\n\n");
  printf(
    "- Options must be the first string on the line and must be written\n"
    "exactly as shown below; the options are case-sensitive.\n"
    "- All characters to the right of a # sign are treated as a comment\n"
    "and are ignored. Blank lines are also ignored.\n"
    "- Options that take an array of arguments may span multiple lines if a $ is\n"
    "placed at the end of the line.\n"
    "- Output parameters (the arguments to %s) are not case sensitive,and\n",
      options[OPT_OUTPUTORDER].cName);
  printf("need only enough characters to be unambiguous.\n\n");

  printf("Output File Structure\n");
  printf("=====================\n\n");
  printf("Output files consist columns of data separated by white space in\n"
    "the same order as listed in %s.\n\n",options[OPT_OUTPUTORDER].cName);
  printf("Input Options\n");
  printf("=============\n\n");
  HelpOptions(options,bLong);

  printf("\n\nOutput Parameters\n");
  printf("=====================\n\n");
  if (!bLong) {
    printf("Format: [Negative forces units] Name -- Description [Negative unit]\n\n");
  }
  printf("These options follow the argument %s.\n",options[OPT_OUTPUTORDER].cName);
  HelpOutput(output,bLong);

  exit(0);
}

/*
 * I/O
 */

void LineExit(char cFile[],int iLine) {
  fprintf(stderr,"\t%s: Line %d\n",cFile,iLine+1);
  exit(EXIT_INPUT);
}

char *sLower(char cString[]) {
  int iPos;
  for (iPos=0;cString[iPos];iPos++)
  cString[iPos] = tolower(cString[iPos]);

  return cString;
}

void fprintd(FILE *fp,double x,int iExp,int iDig) {
  double dMin,dMax;

  dMax=pow(10,iExp);
  dMin=pow(10,-iExp);
  if ((fabs(x) > dMax || fabs(x) < dMin) && x != 0) {
    if (iDig == 0)
      fprintf(fp,"%.0e",x);
    if (iDig == 1)
      fprintf(fp,"%.1e",x);
    if (iDig == 2)
      fprintf(fp,"%.2e",x);
    if (iDig == 3)
      fprintf(fp,"%.3e",x);
    if (iDig == 4)
      fprintf(fp,"%.4e",x);
    if (iDig == 5)
      fprintf(fp,"%.5e",x);
    if (iDig == 6)
      fprintf(fp,"%.6e",x);
    if (iDig == 7)
      fprintf(fp,"%.7e",x);
    if (iDig == 8)
      fprintf(fp,"%.8e",x);
    if (iDig == 9)
      fprintf(fp,"%.9e",x);
    if (iDig == 10)
      fprintf(fp,"%.10e",x);
    if (iDig == 11)
      fprintf(fp,"%.11e",x);
    if (iDig == 12)
      fprintf(fp,"%.12e",x);
    if (iDig == 13)
      fprintf(fp,"%.13e",x);
    if (iDig == 14)
      fprintf(fp,"%.14e",x);
    if (iDig == 15)
      fprintf(fp,"%.15e",x);
    if (iDig == 16)
      fprintf(fp,"%.16e",x);
  } else {
    if (iDig == 0)
      fprintf(fp,"%.0lf",x);
    if (iDig == 1)
      fprintf(fp,"%.1lf",x);
    if (iDig == 2)
      fprintf(fp,"%.2lf",x);
    if (iDig == 3)
      fprintf(fp,"%.3lf",x);
    if (iDig == 4)
      fprintf(fp,"%.4lf",x);
    if (iDig == 5)
      fprintf(fp,"%.5lf",x);
    if (iDig == 6)
      fprintf(fp,"%.6lf",x);
    if (iDig == 7)
      fprintf(fp,"%.7lf",x);
    if (iDig == 8)
      fprintf(fp,"%.8lf",x);
    if (iDig == 9)
      fprintf(fp,"%.9lf",x);
    if (iDig == 10)
      fprintf(fp,"%.10lf",x);
    if (iDig == 11)
      fprintf(fp,"%.11lf",x);
    if (iDig == 12)
      fprintf(fp,"%.12lf",x);
    if (iDig == 13)
      fprintf(fp,"%.13lf",x);
    if (iDig == 14)
      fprintf(fp,"%.14lf",x);
    if (iDig == 15)
      fprintf(fp,"%.15lf",x);
    if (iDig == 16)
      fprintf(fp,"%.16lf",x);
  }
}

/*
 * Unit Conversions
 */

/* Return proper length conversion */
double fdUnitsLength(int iType) {
  if (iType == 0)
    return 1;
  else if (iType == 1)
    return 0.1;
  else if (iType == 2)
    return 1e5;
  else if (iType == 3)
    return RSUN;
  else if (iType == 4)
    return REARTH;
  else if (iType == 5)
    return RJUP;
  else if (iType == 6)
    return AUM;
  else {
    fprintf(stderr,"ERROR: Unknown iUnitLength %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsLength(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"m");
  else if (iType == 1)
    sprintf(cUnit,"cm");
  else if (iType == 2)
    sprintf(cUnit,"km");
  else if (iType == 3)
    sprintf(cUnit,"Rsun");
  else if (iType == 4)
    sprintf(cUnit,"Rearth");
  else if (iType == 5)
    sprintf(cUnit,"Rjupiter");
  else if (iType == 6)
    sprintf(cUnit,"au");
  else {
    fprintf(stderr,"ERROR: Unknown iUnitLength %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

/* Return proper time conversion */
double fdUnitsTime(int iType) {
  if (iType == 0)
    return 1;
  else if (iType == 1)
    return DAYSEC;
  else if (iType == 2)
    return YEARSEC;
  else if (iType == 3)
    return 1e6*YEARSEC;
  else if (iType == 4)
    return 1e9*YEARSEC;
  else {
    fprintf(stderr,"ERROR: Unknown iUnitTime: %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsTime(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"sec");
  else if (iType == 1)
    sprintf(cUnit,"day");
  else if (iType == 2)
    sprintf(cUnit,"year");
  else if (iType == 3)
    sprintf(cUnit,"Myr");
  else if (iType == 4)
    sprintf(cUnit,"Gyr");
  else {
    fprintf(stderr,"ERROR: Unknown iUnitTime: %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

double fdUnitsMass(int iType) {
  if (iType == 0)
    return 1;
  else if (iType == 1)
    return 1e-3;
  else if (iType == 2)
    return MSUN;
  else if (iType == 3)
    return MEARTH;
  else if (iType == 4)
    return MJUP;
  else if (iType == 5)
    return MNEP;
  else {
    fprintf(stderr,"ERROR: Unknown iUnitMass: %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsMass(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"kg");
  else if (iType == 1)
    sprintf(cUnit,"gm");
  else if (iType == 2)
    sprintf(cUnit,"Msun");
  else if (iType == 3)
    sprintf(cUnit,"Mearth");
  else if (iType == 4)
    sprintf(cUnit,"Mjupiter");
  else {
    fprintf(stderr,"ERROR: Unknown iUnitMass: %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

double fdUnitsAngle(int iType) {
  if (iType == 0)
     return 1;
  else if (iType == 1)
     return DEGRAD;
  else {
    fprintf(stderr,"ERROR: Unknown Angle type %d\n.",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsAngle(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"rad");
  else if (iType == 1)
    sprintf(cUnit,"deg");
  else {
    fprintf(stderr,"ERROR: Unknown Angle type %d\n.",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsViscosity(UNITS *units,char cUnit[]) {
  char cTmp[OUTLEN];

  fsUnitsLength(units->iLength,cUnit);
  strcat(cUnit,"^2/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
}

void fsUnitsAngMom(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsMass(units->iMass,cUnit);
  fsUnitsLength(units->iLength,cTmp);
  strcat(cUnit,"*");
  strcat(cUnit,cTmp);
  strcat(cUnit,"^2/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
}

void fsUnitsDensity(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsMass(units->iMass,cUnit);
  strcat(cUnit,"/");
  fsUnitsLength(units->iLength,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^3");
}

void fsUnitsVel(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsLength(units->iLength,cUnit);
  strcat(cUnit,"/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
}

void fsUnitsRate(int iType,char cUnit[]) {
  char cTmp[OPTLEN];

  sprintf(cUnit,"/");
  fsUnitsTime(iType,cTmp);
  strcat(cUnit,cTmp);
}

void fsUnitsAngRate(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsAngle(units->iAngle,cUnit);
  strcat(cUnit,"/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
}

void fsUnitsEnergy(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsMass(units->iMass,cUnit);
  strcat(cUnit,"*");
  fsUnitsLength(units->iLength,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^2/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^2");
}

double fdUnitsEnergy(int iTime,int iMass,int iLength) {
  return fdUnitsMass(iMass)*fdUnitsLength(iLength)*fdUnitsLength(iLength)/(fdUnitsTime(iTime)*fdUnitsTime(iTime));
}

void fsUnitsPower(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsMass(units->iMass,cUnit);
  strcat(cUnit,"*");
  fsUnitsLength(units->iLength,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^2/");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^3");
}

double fdUnitsPower(int iTime,int iMass,int iLength) {
  return fdUnitsMass(iMass)*fdUnitsLength(iLength)*fdUnitsLength(iLength)/(fdUnitsTime(iTime)*fdUnitsTime(iTime)*fdUnitsTime(iTime));
}

void fsUnitsEnergyFlux(UNITS *units,char cUnit[]) {
  char cTmp[OPTLEN];

  fsUnitsEnergy(units,cUnit);
  strcat(cUnit,"/(");
  fsUnitsLength(units->iLength,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,"^2*");
  fsUnitsTime(units->iTime,cTmp);
  strcat(cUnit,cTmp);
  strcat(cUnit,")");
}

double fdUnitsEnergyFlux(int iTime,int iMass,int iLength) {
  double dTmp;

  dTmp=fdUnitsPower(iTime,iMass,iLength);
  return dTmp/(fdUnitsLength(iLength)*fdUnitsLength(iLength));
}

double fdUnitsTemp(double dTemp,int iOldType,int iNewType) {
  if (iOldType == 0) {
    if (iNewType == 1) {
      /* Kelvin -> Celsius */
      return dTemp - 273;
    } else if (iNewType == 2) {
      /* Kelvin to Farenheit */
      return (dTemp - 273)*1.8 + 32;
    } else if (iNewType == 0) {
      return dTemp;
    } else {
      fprintf(stderr,"ERROR: Unknown Temperature type %d.\n",iNewType);
      exit(EXIT_UNITS);
    }
  } else if (iOldType == 1) {
    if (iNewType == 0) {
      /* Celsius -> Kelvin */
      return dTemp + 273;
    } else if (iNewType == 2) {
      /* Celsius -> Farenheit */
      return (1.8*dTemp) + 32;
    } else if (iNewType == 1) {
      return dTemp;
    } else {
      fprintf(stderr,"ERROR: Unknown Temperature type %d.\n",iNewType);
      exit(EXIT_UNITS);
    }
  } else if (iOldType == 2) {
    if (iNewType == 0) {
      /* Farenheit -> Kelvin */
      return 5/9*(dTemp - 32) + 273;
    } else if (iNewType == 1) {
      /* Farenheit -> Celsius */
      return 5/9*(dTemp - 32);
    } else if (iNewType == 2) {
      return dTemp;
    } else {
      fprintf(stderr,"ERROR: Unknown Temperature type %d.\n",iNewType);
      exit(EXIT_UNITS);
    }
  } else {
    fprintf(stderr,"ERROR: Unknown Temperature type %d.\n",iOldType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsTemp(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"K");
  else if (iType == 1)
    sprintf(cUnit,"C");
  else if (iType == 2)
    sprintf(cUnit,"F");
  else {
    fprintf(stderr,"ERROR: Unknown iUnitTemp %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

void fsUnitsTempRate(int iType,char cUnit[]) {
  if (iType == 0)
    sprintf(cUnit,"K/s");
  else if (iType == 1)
    sprintf(cUnit,"C/s");
  else if (iType == 2)
    sprintf(cUnit,"F/s");
  else {
    fprintf(stderr,"ERROR: Unknown iUnitTempRate %d.\n",iType);
    exit(EXIT_UNITS);
  }
}

/*
 * FILES struct functions
 */

void InfileCopy(INFILE *dest,INFILE *src) {
  int iLine;

  strcpy(dest->cIn,src->cIn);
  for (iLine=0;iLine<src->iNumLines;iLine++)
    dest->bLineOK[iLine] = src->bLineOK[iLine];

  /* PHOTOCHEM fields
  strcpy(dest->cSpecies,src->cSpecies);
  strcpy(dest->cReactions,src->cReactions);
  */
}
