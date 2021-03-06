from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckSMPStatus():
    print("Which beam do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.Beams):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            GetSMPStatus("Beam 1")
        elif int(selection) == 2:
            GetSMPStatus("Beam 2")
        else:
            pass

def GetSMPStatus(Beam):
    if Beam == "Beam 1":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
        rgb_img = img.convert('RGB')
        coords = [
            (872,572),  #Stable Beams
            (872,600),  #Moveable Devices Allowed In
            (872,629),  #Beam Presence
            (872,658),  #Setup Beam
            (872,686),  #Global Beam Permit
            (872,715)   #Link Status of Beam Permits
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        if colors[5].g == 255:
            del colors[3]   #if in stable beams remove the setup flag
        elif len(colors) == 6 & colors[3].g == 255:
            del colors[5]   #if in setup remove the stable beams flag

        for color in colors:
            if color.r == 255:
                print("There is a fault with Beam 1's SMP status")
                return
        print("Beam 1's SMP status is good.")

    elif Beam == "Beam 2":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
        rgb_img = img.convert('RGB')
        coords = [
            (945,572),  #Stable Beams
            (945,600),  #Moveable Devices Allowed in
            (945,629),  #Beam Presence
            (945,658),  #Setup Beam
            (945,686),  #Global Beam Permit
            (945,715)   #Link Status of Beam Permits
        ]
        colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

        if colors[5].g == 255:
            del colors[3]   #if in stable beams remove the setup flag
        elif len(colors) == 6 & colors[3].g == 255:
            del colors[5]   #if in setup remove the stable beams flag

        for color in colors:
            if color.r == 255:
                print("There is a fault with Beam 2's SMP status")
                return
        print("Beam 2's SMP status is good.")

def CheckSMPIndividual():
    print("Which beam dump do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.Beams):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            print("Which SMP Flag do you want to check?")
            i = 0
            for Option in (LHCStatusOptions.SMPFlags):
                i += 1
                print('{}. {}'.format(i,Option.name.replace('_',' ')))

            selection = input()

            if selection.isdigit():
                if int(selection) == 1:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Link_Status_of_Beam_Permits)
                elif int(selection) == 2:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Global_Beam_Permit)
                elif int(selection) == 3:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Setup_Beam)
                elif int(selection) == 4:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Beam_Presence)
                elif int(selection) == 5:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Moveable_Devices_Allowed_In)
                elif int(selection) == 6:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam1, LHCStatusOptions.SMPFlags.Stable_Beams)
                else:
                    pass
        elif int(selection) == 2:
            print("Which SMP Flag do you want to check?")
            i = 0
            for Option in (LHCStatusOptions.SMPFlags):
                i += 1
                print('{}. {}'.format(i,Option.name.replace('_',' ')))

            selection = input()

            if selection.isdigit():
                if int(selection) == 1:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Link_Status_of_Beam_Permits)
                elif int(selection) == 2:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Global_Beam_Permit)
                elif int(selection) == 3:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Setup_Beam)
                elif int(selection) == 4:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Beam_Presence)
                elif int(selection) == 5:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Moveable_Devices_Allowed_In)
                elif int(selection) == 6:
                    GetSMPStatusIndividual(LHCStatusOptions.Beams.Beam2, LHCStatusOptions.SMPFlags.Stable_Beams)
                else:
                    pass
        else:
            pass

def GetSMPStatusIndividual(beam, smpflag):
    if beam == LHCStatusOptions.Beams.Beam1:
        if smpflag == LHCStatusOptions.SMPFlags.Link_Status_of_Beam_Permits:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,572))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Global_Beam_Permit:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,600))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Setup_Beam:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,629))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Beam_Presence:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,658))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Moveable_Devices_Allowed_In:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,686))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Stable_Beams:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((872,715))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        else:
            pass
    elif beam == LHCStatusOptions.Beams.Beam2:
        if smpflag == LHCStatusOptions.SMPFlags.Link_Status_of_Beam_Permits:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,572))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Global_Beam_Permit:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,600))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Setup_Beam:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,629))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Beam_Presence:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,658))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Moveable_Devices_Allowed_In:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,686))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        elif smpflag == LHCStatusOptions.SMPFlags.Stable_Beams:
            img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
            rgb_img = img.convert('RGB')
            if Color(*rgb_img.getpixel((945,715))).g == 255:
                print("{} flag is true.".format(smpflag.name.replace('_',' ')))
            else:
                print("{} flag is false.".format(smpflag.name.replace('_',' ')))
        else:
            pass
    else:
        pass