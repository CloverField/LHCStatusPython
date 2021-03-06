"""Pulls information from the LHC Vistars website and lets the user know the 
status of the machine.
..moduleauthor:: CloverField
"""

#import LHCStatusOptions
from CheckCryo import CheckCryo
from CheckCryoIndividual import CheckCryoIndividual
from Check60AmpPCPermit import Check60AmpPCPermit, Check60AmpPCPermitIndividual
from CheckRFStatus import CheckRFStatus, CheckRFStatusIndividual
from CheckBeamDumpStatus import CheckBeamDumpStatus, CheckBeamDumpIndividual
from CheckExpMagnetStatus import CheckExpMagnetStatus, CheckExpMagnetIndividual
from CheckSMPStatus import CheckSMPStatus, CheckSMPIndividual
from CheckVistarPage import CheckVistarPage, CheckVistarComments

def main():
    """
    The main method for the program. Asks the user what part of the machine
    they want to check.
    """
    print("What do you want to check?")
    print("1. Cryo Status")
    print("2. Individual Cryo Status")
    print("3. 60 Amp PC Permit Status")  
    print("4. Individual 60 Amp PC Permit Status")
    print("5. RF Status")
    print("6. RF Status Individual")
    print("7. Beam Dump Status")
    print("8. Beam Dump Component Status")
    print("9. Experiment Magnet Status")
    print("10. Individual Experiment Magnet Status")
    print("11. Page 1 Beam SMP Status")
    print("12. Page 1 Individual SMP Beam Status")
    print("13. Perform OCR on LHC Vistar page")
    print("14. Perform OCR on LHC vistar page comments")

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            CheckCryo()
        elif int(selection) == 2:
            CheckCryoIndividual()
        elif int(selection) == 3:
            Check60AmpPCPermit()
        elif int(selection) == 4:
            Check60AmpPCPermitIndividual()
        elif int(selection) == 5:
            CheckRFStatus()
        elif int(selection) == 6:
            CheckRFStatusIndividual()
        elif int(selection) == 7:
            CheckBeamDumpStatus()    
        elif int(selection) == 8:
            CheckBeamDumpIndividual()    
        elif int(selection) == 9:
            CheckExpMagnetStatus()    
        elif int(selection) == 10:
            CheckExpMagnetIndividual()    
        elif int(selection) == 11:
            CheckSMPStatus()    
        elif int(selection) == 12:
            CheckSMPIndividual()  
        elif int(selection) == 13:
            CheckVistarPage()    
        elif int(selection) == 14:
            CheckVistarComments()    
        else:
            pass


if __name__ == "__main__":
    main()