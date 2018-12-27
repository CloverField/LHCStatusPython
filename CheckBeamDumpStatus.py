from Web import getImage
from Color import Color

def CheckBeamDumpStatus():
    print("Which beam dump do you want to check?")
    print("1. Beam 1")
    print("2. Beam 2")

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            GetBeamDumpStatus("Beam 1")
        elif int(selection) == 2:
            GetBeamDumpStatus("Beam 2")
        else:
            pass

def GetBeamDumpStatus(Beam):
    if Beam == "Beam 1":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        coords = [
            (192,38),   #BeamOneDumped
            (73,60),    #Kicker
            (200,60),   #BETS
            (323,60),   #IPOC - Beam Dump Pane
            (76,80),    #LASS
            (200,82),   #RETRIGGER
            (326,82),   #XPOC
            (81,101),   #REMOTE - Beam Dump Pane
            (193,102),  #ON - Beam Dump Pane
            (90,168),   #REMOTE - Injection Pane
            (194,168),  #ON - Injection Pane
            (333,168),  #TIMING ON
            (65,189),   #CONDITIONING
            (286,188),  #TIMEOUT
            (111,210),  #IPOC - Injection Pane
            (290,210)   #IQC
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like there is a error with the Beam 1 Beam Dump.")
                return
        print("Everything looks good for the Beam 1 Beam Dump.")
        
    elif Beam == "Beam 2":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        coords = [
            (593, 38),  #BeamTwoDumped
            (472,60),   #Kicker
            (600,60),   #BETS
            (723,60),   #IPOC - Beam Dump Pane
            (476,80),   #LASS
            (600,82),   #RETRIGGER
            (726,82),   #XPOC
            (481,101),  #REMOTE - Beam Dump Pane
            (593,102),  #ON - Beam Dump Pane
            (490,168),  #REMOTE - Injection Pane
            (594,168),  #ON - Injection Pane
            (733,168),  #TIMING ON
            (465,189),  #CONDITIONING
            (686,188),  #TIMEOUT
            (511,210),  #IPOC - Injection Pane
            (690,210)   #IQC
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        for color in colors:
            if color.r == 255:
                print("Looks like there is a error with the Beam 2 Beam Dump.")
                return
        print("Everything looks good for the Beam 2 Beam Dump.")