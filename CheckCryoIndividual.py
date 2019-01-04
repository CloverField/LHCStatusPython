import LHCStatusOptions
from Color import Color
from Web import getImage

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
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((100,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CSITR1:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((188,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CMMSR1:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((288,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CSMSR1:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((378,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CMAR12:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((478,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CSAR12:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((568,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CMMSL2:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((668,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CSMSL2:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((758,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CMITL2:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((858,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))

    elif sector == LHCStatusOptions.Sector12Magnets.CSITL2:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((948,100))).g == 255:
            print("Everything looks good for {}.".format(sector.name))
        else:
            print("Cryo is down for {}.".format(sector.name))
            
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

    if sector == LHCStatusOptions.Sector67Magnets.CMMSR6:
        print("Found Magnet")
    elif sector == LHCStatusOptions.Sector67Magnets.CSMSR6:
        pass
    elif sector == LHCStatusOptions.Sector67Magnets.CMAML7:
        pass
    elif sector == LHCStatusOptions.Sector67Magnets.CSAML7:
        pass
    else:
        pass

    if sector == LHCStatusOptions.Sector78Magnets.CMAMR7:
        print("Found magnet")
    elif sector == LHCStatusOptions.Sector78Magnets.CSAMR7:
        pass
    elif sector == LHCStatusOptions.Sector78Magnets.CMMSL8:
        pass
    elif sector == LHCStatusOptions.Sector78Magnets.CSMSL8:
        pass
    elif sector == LHCStatusOptions.Sector78Magnets.CMITL8:
        pass
    elif sector == LHCStatusOptions.Sector78Magnets.CSITL8:
        pass
    else:
        pass

    if sector == LHCStatusOptions.Sector81Magnets.CMITR8:
        print("Found Magnet")
    elif sector == LHCStatusOptions.Sector81Magnets.CSITR8:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CMMSR8:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CSMSR8:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CMAR81:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CSAR81:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CMMSL1:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CSMSL1:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CMITL1:
        pass
    elif sector == LHCStatusOptions.Sector81Magnets.CSITL1:
        pass
    else:
        pass