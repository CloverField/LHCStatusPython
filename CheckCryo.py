"""
.. module:: CheckCryo
    :platform: MacOS ,Windows, Unix
    :synopsis: The CheckCryo module. Returns information about the cryo state of each sector. 
.. moduleauthor:: CloverField
"""
from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckCryo():
    """
    Prompts the user for which sector to check. 
    Then calls the appropriate :func:`GetSectorStatus` to check the status of the sector 
    """

    print("Which Sector do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.Sectors):
        i += 1
        print('{}. {}'.format(i,Option.value))

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
    """
    This function checks the individual cryostats for the sector.
    It lets the user know if all the cryostats are good or if one is faulty.
    :param Sector: the Sector to check.
    :type Sector: Sector:`LHCStatusOperations.Sectors`
    """

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
