#import LHCStatusOptions
from CheckCryo import CheckCryo

def main():
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
    print("13. Performs OCR on LHC Vistar page")

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            print("Selected Check Cryo")
            CheckCryo()
        elif int(selection) == 2:
            pass
        else:
            pass


if __name__ == "__main__":
    main()