from enum import Enum, auto

class StatusOptions(Enum):
    CryoStatus = "Cryo Status"
    CryoStatusIndividual = "Individual Cryo Status"
    PCPermitStatus = "60 Amp PC Permit Status"  
    PCPermitStatusIndividual = "Individual 60 Amp PC Permit Status" 
    RFStatus = "RF Status"
    RFStatusIndividual = "RF Status Individual" 
    BeamDumpStatus = "Beam Dump Status"
    BeamDumpComponentStatus = "Beam Dump Component Status"
    EXPMagnetStatus = "Experiment Magnet Status"
    EXPMagnetIndivdualStatus = "Individual Experiment Magnet Status"
    Page1BeamStatus = "Page 1 Beam SMP Status"
    Page1BeamSMPStatus = "Page 1 Individual SMP Beam Status"
    PerformOCROnVistarPage = "Performs OCR on LHC Vistar page"

class Sectors(Enum):
    Sector12 = "Sector 12"
    Sector23 = "Sector 23"
    Sector34 = "Sector 34"
    Sector45 = "Sector 45"
    Sector56 = "Sector 56"
    Sector67 = "Sector 67"
    Sector78 = "Sector 78"
    Sector81 = "Sector 81"

class Sector12Magnets(Enum):
    CMITR1 = auto()
    CSITR1 = auto()
    CMMSR1 = auto()
    CSMSR1 = auto()
    CMAR12 = auto()
    CSAR12 = auto()
    CMMSL2 = auto()
    CSMSL2 = auto()
    CMITL2 = auto()
    CSITL2 = auto()

class Sector23Magnets(Enum):
    CMITR2 = auto()
    CSITR2 = auto()
    CMMSR2 = auto()
    CSMSR2 = auto()
    CMAML3 = auto()
    CSAML3 = auto()

class Sector34Magnets(Enum):
    CMAMR3 = auto()
    CSAMR3 = auto()
    CMMSL4 = auto()
    CSMSL4 = auto()

class Sector45Magnets(Enum):
    CMMSR4 = auto()
    CSMSR4 = auto()
    CMAR45 = auto()
    CSAR45 = auto()
    CMMSL5 = auto()
    CSMSL5 = auto()
    CMITL5 = auto()
    CSITL5 = auto()

class Sector56Magnets(Enum):
    CMITR5 = auto()
    CSITR5 = auto()
    CMMSR5 = auto()
    CSMSR5 = auto()
    CMAR56 = auto()
    CSAR56 = auto()
    CMMSL6 = auto()
    CSMSL6 = auto()

## Will need to make a new class that contains a value and a string