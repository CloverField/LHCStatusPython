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

class RFSectors(Enum):
    Sector1L4 = "Sector 1L4"
    Sector1R4 = "Sector 1R4"
    Sector2L4 = "Sector 2L4"
    Sector2R4 = "Sector 2R4"

class RFCryo(Enum):
    CM1L4 = auto()
    CS1L4 = auto()
    CM2L4 = auto()
    CS2L4 = auto()
    CM1R4 = auto()
    CS1R4 = auto()
    CM2R4 = auto()
    CS2R4 = auto()

class Beams(Enum):
    Beam1 = "Beam 1"
    Beam2 = "Beam 2"

class Components(Enum):
    BeamDumped = "BeamDumped"
    Kicker = "Kicker"
    BETS = "BETS"
    IPOC_U_Beam_Dump_Pane = "IPOC - Beam Dump Pane"
    LASS = "LASS"
    RETRIGGER = "RETRIGGER"
    XPOC = "XPOC"
    REMOTE_U_Beam_Dump_Pane = "REMOTE - Beam Dump Pane"
    ON_U_Beam_Dump_Pane = "ON - Beam Dump Pane"
    REMOTE_U_Injection_Pane = "REMOTE - Injection Pane"
    ON_U_Injection_Pane = "ON - Injection Pane"
    TIMING_ON = "TIMING ON"
    CONDITIONING = "CONDITIONING"
    TIMEOUT = "TIMEOUT"
    IPOC_U_Injection_Pane = "IPOC - Injection Pane"
    IQC = "IQC"

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

class Sector67Magnets(Enum):
    CMMSR6 = auto()
    CSMSR6 = auto()
    CMAML7 = auto()
    CSAML7 = auto()

class Sector78Magnets(Enum):
    CMAMR7 = auto()
    CSAMR7 = auto()
    CMMSL8 = auto()
    CSMSL8 = auto()
    CMITL8 = auto()
    CSITL8 = auto()

class Sector81Magnets(Enum):
    CMITR8 = auto()
    CSITR8 = auto()
    CMMSR8 = auto()
    CSMSR8 = auto()
    CMAR81 = auto()
    CSAR81 = auto()
    CMMSL1 = auto()
    CSMSL1 = auto()
    CMITL1 = auto()
    CSITL1 = auto()

class EXPMagnets(Enum):
    ALICE_solenoid = auto()
    ALICE_dipole = auto()
    ATLAS_solenoid = auto()
    ATLAS_torid = auto()
    CMS_solenoid = auto()
    LHCb_dipole = auto()

class SMPFlags(Enum):
    Link_Status_of_Beam_Permits = auto()
    Global_Beam_Permit = auto()
    Setup_Beam = auto()
    Beam_Presence = auto()
    Moveable_Devices_Allowed_In = auto()
    Stable_Beams = auto()

## Will need to make a new class that contains a value and a string