from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckBeamDumpStatus():
    print("Which beam dump do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.Beams):
        i += 1
        print('{}. {}'.format(i,Option.value))

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

def CheckBeamDumpIndividual():
    print("Which beam dump do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.Beams):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            print("Which component do you want to check?")
            i = 0
            for Option in (LHCStatusOptions.Components):
                i += 1
                print('{}. {}'.format(i,Option.value))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.BeamDumped)
                elif int(selection) == 2:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.Kicker)
                elif int(selection) == 3:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.BETS)
                elif int(selection) == 4:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.IPOC_U_Beam_Dump_Pane)
                elif int(selection) == 5:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.LASS)
                elif int(selection) == 6:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.RETRIGGER)
                elif int(selection) == 7:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.XPOC)
                elif int(selection) == 8:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.REMOTE_U_Beam_Dump_Pane)
                elif int(selection) == 9:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.ON_U_Beam_Dump_Pane)
                elif int(selection) == 10:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.REMOTE_U_Injection_Pane)
                elif int(selection) == 11:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.ON_U_Injection_Pane)
                elif int(selection) == 12:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.TIMING_ON)
                elif int(selection) == 13:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.CONDITIONING)
                elif int(selection) == 14:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.TIMEOUT)
                elif int(selection) == 15:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.IPOC_U_Injection_Pane)
                elif int(selection) == 16:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.Components.IQC)

        elif int(selection) == 2:
            print("Which component do you want to check?")
            i = 0
            for Option in (LHCStatusOptions.Components):
                i += 1
                print('{}. {}'.format(i,Option.value))

            selection = input()
            if selection.isdigit():
                if int(selection) == 1:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.BeamDumped)
                elif int(selection) == 2:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.Kicker)
                elif int(selection) == 3:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.BETS)
                elif int(selection) == 4:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.IPOC_U_Beam_Dump_Pane)
                elif int(selection) == 5:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.LASS)
                elif int(selection) == 6:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.RETRIGGER)
                elif int(selection) == 7:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.XPOC)
                elif int(selection) == 8:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.REMOTE_U_Beam_Dump_Pane)
                elif int(selection) == 9:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.ON_U_Beam_Dump_Pane)
                elif int(selection) == 10:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.REMOTE_U_Injection_Pane)
                elif int(selection) == 11:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.ON_U_Injection_Pane)
                elif int(selection) == 12:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.TIMING_ON)
                elif int(selection) == 13:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.CONDITIONING)
                elif int(selection) == 14:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.TIMEOUT)
                elif int(selection) == 15:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.IPOC_U_Injection_Pane)
                elif int(selection) == 16:
                    GetBeamDumpStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.Components.IQC)

    else:
        pass

def GetBeamDumpStatusIndividual(beam, component):
    if beam == LHCStatusOptions.Beams.Beam1:
        if component == LHCStatusOptions.Components.BeamDumped:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((192,38))).g == 255:
                print("{} has not been dumped.".format(beam.value))
            else:
                print("{} has been dumped.".format(beam.value))
        elif component == LHCStatusOptions.Components.Kicker:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((73,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.BETS:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((200,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.IPOC_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((323,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.LASS:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((76,80))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.RETRIGGER:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((200,82))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.XPOC:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((326,82))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.REMOTE_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((81,101))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.ON_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((193,102))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.REMOTE_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((90,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.ON_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((194,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.TIMING_ON:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((333,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.CONDITIONING:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((65,189))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.TIMEOUT:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((286,188))).g == 255:
                print("The {} has not expired.".format(component.value))
            else:
                print("The {} has expired.".format(component.value))
        elif component == LHCStatusOptions.Components.IPOC_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((111,210))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.IQC:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((290,210))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        else:
            pass

    elif beam == LHCStatusOptions.Beams.Beam2:
        if component == LHCStatusOptions.Components.BeamDumped:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((593,38))).g == 255:
                print("{} has not been dumped.".format(beam.value))
            else:
                print("{} has been dumped.".format(beam.value))
        elif component == LHCStatusOptions.Components.Kicker:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((472,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.BETS:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((600,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.IPOC_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((723,60))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.LASS:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((476,80))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.RETRIGGER:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((600,82))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.XPOC:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((726,82))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.REMOTE_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((481,101))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.ON_U_Beam_Dump_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((593,102))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.REMOTE_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((490,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.ON_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((594,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.TIMING_ON:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((733,168))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.CONDITIONING:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((465,189))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.TIMEOUT:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((686,188))).g == 255:
                print("The {} has not expired.".format(component.value))
            else:
                print("The {} has expired.".format(component.value))
        elif component == LHCStatusOptions.Components.IPOC_U_Injection_Pane:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((511,210))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        elif component == LHCStatusOptions.Components.IQC:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((690,210))).g == 255:
                print("The {} is good.".format(component.value))
            else:
                print("The {} is faulty.".format(component.value))
        else:
            pass

    else:
        pass