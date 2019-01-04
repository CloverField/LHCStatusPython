from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckCryo():
    print("Which Sector do you want to check?")
    print("1. Sector 12")
    print("2. Sector 23")
    print("3. Sector 34")
    print("4. Sector 45")
    print("5. Sector 56")
    print("6. Sector 67")
    print("7. Sector 78")
    print("8. Sector 81")

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            GetSectorStatus("Sector 12")
        elif int(selection) == 2:
            GetSectorStatus("Sector 23")
        elif int(selection) == 3:
            GetSectorStatus("Sector 34")
        elif int(selection) == 4:
            GetSectorStatus("Sector 45")
        elif int(selection) == 5:
            GetSectorStatus("Sector 56")
        elif int(selection) == 6:
            GetSectorStatus("Sector 67")
        elif int(selection) == 7:
            GetSectorStatus("Sector 78")
        elif int(selection) == 8:
            GetSectorStatus("Sector 81")
        else:
            pass

def GetSectorStatus(Sector):

    if Sector == "Sector 12":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (100,100),  #CMITR1
            (188,100),  #CSITR1
            (288,100),  #CMMSR1
            (378,100),  #CSMSR1
            (478,100),  #CMAR12
            (568,100),  #CSAR12
            (668,100),  #CMMSL2
            (758,100),  #CSMSL2
            (858,100),  #CMITL2
            (948,100)   #CSITL2
        ] 
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 12.")
                return
        print("Everything looks good in Sector 12.")

    elif Sector == "Sector 23":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (100,140),  #CMITR2
            (188,140),  #CSITR2
            (288,140),  #CMMSR2
            (378,140),  #CSMSR2
            (478,140),  #CMAML3
            (568,140)   #CSAML3
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 23.")
                return
        print("Everything looks good in Sector 23.")

    elif Sector == "Sector 34":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (478,175),  #CMAML3
            (568,175),  #CSAML3
            (668,175),  #CMMSL1
            (758,175)   #CSMSL1
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 34.")
                return
        print("Everything looks good in Sector 34.")

    elif Sector == "Sector 45":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (288,210),  #CMMSR4
            (378,210),  #CSMSR4
            (478,210),  #CMAR45
            (568,210),  #CSAR45
            (668,210),  #CMMSL5
            (758,210),  #CSMSL5
            (858,210),  #CMITL6
            (948,210)   #CSITL6
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 45.")
                return
        print("Everything looks good in Sector 45.")

    elif Sector == "Sector 56":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (100,245),  #CMITR5
            (188,245),  #CSITR5
            (288,245),  #CMMSR5
            (378,245),  #CSMSR5
            (478,245),  #CMAR56
            (568,245),  #CSAR56
            (668,245),  #CMMSL6
            (758,245)   #CSMSL6
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 56.")
                return
        print("Everything looks good in Sector 56.")

    elif Sector == "Sector 67":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (288,280),  #CMMSR6
            (378,280),  #CSMSR6
            (478,280),  #CMAML7
            (568,280)   #CSAML7
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 67.")
                return
        print("Everything looks good in Sector 67.")

    elif Sector == "Sector 78":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (478,315),  #CMAMR7
            (568,315),  #CSAMR7
            (668,315),  #CMMSL8
            (758,315),  #CSMSL8
            (858,315),  #CMITL8
            (948,315)   #CSITL8
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 78.")
                return
        print("Everything looks good in Sector 78.")

    elif Sector == "Sector 81":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        coords = [
            (100,350),  #CMITR8
            (188,350),  #CSITR8
            (288,350),  #CMMSR8
            (378,350),  #CSMSR8
            (478,350),  #CMAR81
            (568,350),  #CSAR81
            (668,350),  #CMMSL1
            (758,350),  #CSMSL1
            (858,350),  #CMITL1
            (948,350)   #CSITL1
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 81.")
                return
        print("Everything looks good in Sector 81.")

def CheckCryoIndividual():
    i = 0
    print("Which Sector do you want to check?")
    for Option in (LHCStatusOptions.Sectors):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()
    i = 0

    if selection.isdigit():
        if int(selection) == 1:
            print("Which Magnet do you want to check in Sector 12?")
            for Option in (LHCStatusOptions.Sector12Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CMITR1)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CSITR1)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CMMSR1)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CSMSR1)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CMAR12)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CSAR12)
                elif int(selection) == 7:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CMMSL2)
                elif int(selection) == 8:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CSMSL2)
                elif int(selection) == 9:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CMITL2)
                elif int(selection) == 10:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector12Magnets.CSITL2)
                else:
                    pass

        elif int(selection) == 2:
            print("Which Magnet do you want to check in Sector 23?")
            for Option in (LHCStatusOptions.Sector23Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CMITR2)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CSITR2)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CMMSR2)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CSMSR2)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CMAML3)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector23Magnets.CSAML3)
                else:
                    pass

        elif int(selection) == 3:
            print("Which Magnet do you want to check in Sector 34?")
            for Option in (LHCStatusOptions.Sector34Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector34Magnets.CMAMR3)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector34Magnets.CSAMR3)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector34Magnets.CMMSL4)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector34Magnets.CSMSL4)
                else:
                    pass

        elif int(selection) == 4:
            print("Which Magnet do you want to check in Sector 45?")
            for Option in (LHCStatusOptions.Sector45Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CMMSR4)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CSMSR4)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CMAR45)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CSAR45)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CMMSL5)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CSMSL5)
                elif int(selection) == 7:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CMITL5)
                elif int(selection) == 8:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector45Magnets.CSITL5)
                else:
                    pass

        elif int(selection) == 5:
            print("Which Magnet do you want to check in Sector 56?")
            for Option in (LHCStatusOptions.Sector56Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CMITR5)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CSITR5)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CMMSR5)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CSMSR5)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CMAR56)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CSAR56)
                elif int(selection) == 7:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CMMSL6)
                elif int(selection) == 8:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector56Magnets.CSMSL6)
                else:
                    pass

        elif int(selection) == 6:
            print("Which Magnet do you want to check in Sector 67?")
            for Option in (LHCStatusOptions.Sector67Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector67Magnets.CMMSR6)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector67Magnets.CSMSR6)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector67Magnets.CMAML7)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector67Magnets.CSAML7)
                else:
                    pass

        elif int(selection) == 7:
            print("Which Magnet do you want to check in Sector 78?")
            for Option in (LHCStatusOptions.Sector78Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CMAMR7)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CSAMR7)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CMMSL8)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CSMSL8)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CMITL8)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector78Magnets.CSITL8)
                else:
                    pass

        elif int(selection) == 8:
            print("Which Magnet do you want to check in Sector 81?")
            for Option in (LHCStatusOptions.Sector81Magnets):
                i += 1
                print('{}. {}'.format(i,Option.name))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CMITR8)
                elif int(selection) == 2:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CSITR8)
                elif int(selection) == 3:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CMMSR8)
                elif int(selection) == 4:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CSMSR8)
                elif int(selection) == 5:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CMAR81)
                elif int(selection) == 6:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CSAR81)
                elif int(selection) == 7:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CMMSL1)
                elif int(selection) == 8:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CSMSL1)
                elif int(selection) == 9:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CMITL1)
                elif int(selection) == 10:
                    GetSectorStatusIndividual(LHCStatusOptions.Sector81Magnets.CSITL1)
                else:
                    pass

        else:
            pass

    pass

def GetSectorStatusIndividual(sector):
    if sector == LHCStatusOptions.Sector12Magnets.CMITR1:
        print("Found Magnet")
    elif sector == LHCStatusOptions.Sector12Magnets.CSITR1:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CMMSR1:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CSMSR1:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CMAR12:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CSAR12:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CMMSL2:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CSMSL2:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CMITL2:
        pass
    elif sector == LHCStatusOptions.Sector12Magnets.CSITL2:
        pass
    else:
        pass
    
    if sector == LHCStatusOptions.Sector23Magnets.CMITR2:
        print("Found Magnet")
    elif sector == LHCStatusOptions.Sector23Magnets.CSITR2:
        pass
    elif sector == LHCStatusOptions.Sector23Magnets.CMMSR2:
        pass
    elif sector == LHCStatusOptions.Sector23Magnets.CSMSR2:
        pass
    elif sector == LHCStatusOptions.Sector23Magnets.CMAML3:
        pass
    elif sector == LHCStatusOptions.Sector23Magnets.CSAML3:
        pass
    else:
        pass

    if sector == LHCStatusOptions.Sector34Magnets.CMAMR3:
        print("Found Magnet")
    elif sector == LHCStatusOptions.Sector34Magnets.CSAMR3:
        pass
    elif sector == LHCStatusOptions.Sector34Magnets.CMMSL4:
        pass
    elif sector == LHCStatusOptions.Sector34Magnets.CSMSL4:
        pass
    else:
        pass

    if sector == LHCStatusOptions.Sector45Magnets.CMMSR4:
        print("Found magnet")
    elif sector == LHCStatusOptions.Sector45Magnets.CSMSR4:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CMAR45:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CSAR45:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CMMSL5:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CSMSL5:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CMITL5:
        pass
    elif sector == LHCStatusOptions.Sector45Magnets.CSITL5:
        pass
    else:
        pass

    if sector == LHCStatusOptions.Sector56Magnets.CMITR5:
        print("Found magnet")
    elif sector == LHCStatusOptions.Sector56Magnets.CSITR5:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CMMSR5:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CSMSR5:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CMAR56:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CSAR56:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CMMSL6:
        pass
    elif sector == LHCStatusOptions.Sector56Magnets.CSMSL6:
        pass
    else:
        pass