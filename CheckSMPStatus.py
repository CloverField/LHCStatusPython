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