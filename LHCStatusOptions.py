from enum import Enum
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

## Will need to make a new class that contains a value and a string