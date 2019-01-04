from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckRFStatus():
    print("Which Sector do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.RFSectors):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            GetRFStatus("Sector 1L4")
        elif int(selection) == 2:
            GetRFStatus("Sector 1R4")
        elif int(selection) == 3:
            GetRFStatus("Sector 2L4")
        elif int(selection) == 4:
            GetRFStatus("Sector 2R4")
        else:
            pass

def GetRFStatus(Sector):
    if Sector == "Sector 1L4":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (100,440),  #CM1L4
            (188,440)   #CS1L4
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 1L4.")
                return
        print("Everything looks good in Sector 1L4.")
    
    elif Sector == "Sector 1R4":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (480,440),  #CM1R4
            (570,440)   #CS1R4
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 1R4.")
                return
        print("Everything looks good in Sector 1R4.")

    elif Sector == "Sector 2L4":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (290,440),  #CM2L4
            (380,440)   #CS2L4
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 2L4.")
                return
        print("Everything looks good in Sector 2L4.")

    elif Sector == "Sector 2R4":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (670,440),  #CM2R4
            (760,440)   #CS2R4
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 2R4.")
                return
        print("Everything looks good in Sector 2R4.")

def CheckRFStatusIndividual():
    print("Which Cryostat do you want to Check?")
    i = 0
    for Option in (LHCStatusOptions.RFCryo):
        i += 1
        print('{}. {}'.format(i,Option.name))

    selection = input()

    if selection.isdigit():
        if selection == 1:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CM1L4)
        elif selection == 2:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CS1L4)
        elif selection == 3:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CM2L4)
        elif selection == 4:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CS2L4)
        elif selection == 5:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CM1R4)
        elif selection == 6:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CS1R4)
        elif selection == 7:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CM2R4)
        elif selection == 8:
            GetRFStatusIndividual(LHCStatusOptions.RFCryo.CS2R4)
        else:
            pass

def GetRFStatusIndividual(CryoStat):
    pass