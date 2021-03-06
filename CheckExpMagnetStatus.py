from Web import getImage
from Color import Color
import LHCStatusOptions

def CheckExpMagnetStatus():
    GetExpMagnetStatus()

def GetExpMagnetStatus():
    colors = list()
    img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcexpmag.png")
    rgb_img = img.convert('RGB')
    coords = [
        (365,60),   #ALICE solenoid
        (365,100),  #ALICE dipole  
        (365,140),  #ATLAS solenoid
        (365,180),  #ATLAS toroid
        (365,220),  #CMS solenoid
        (365,260)   #LHcb dipole
    ]
    colors += [ Color(*rgb_img.getpixel((xy))) for xy in coords ]

    for color in colors:
        if color.r == 255:
            print("Not all Experiment magnets are functioning correctly.")
            return
    print("All Experiment magnets are functioning correctly.")

def CheckExpMagnetIndividual():
    print("Which magnet do you want to check?")
    i = 0
    for Option in (LHCStatusOptions.EXPMagnets):
        i += 1
        print('{}. {}'.format(i,Option.name.replace('_', ' ')))

    selection = input()

    if selection.isdigit():
        if int(selection) == 1:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.ALICE_solenoid)
        elif int(selection) == 2:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.ALICE_dipole)
        elif int(selection) == 3:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.ATLAS_solenoid)
        elif int(selection) == 4:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.ATLAS_torid)
        elif int(selection) == 5:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.CMS_solenoid)
        elif int(selection) == 6:
            GetExpMagnetStatusIndividual(LHCStatusOptions.EXPMagnets.LHCb_dipole)
        else:
            pass

def GetExpMagnetStatusIndividual(magnet):
    if magnet == LHCStatusOptions.EXPMagnets.ALICE_solenoid:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,60))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    elif magnet == LHCStatusOptions.EXPMagnets.ALICE_dipole:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,100))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    elif magnet == LHCStatusOptions.EXPMagnets.ATLAS_solenoid:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,142))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    elif magnet == LHCStatusOptions.EXPMagnets.ATLAS_torid:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,180))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    elif magnet == LHCStatusOptions.EXPMagnets.CMS_solenoid:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,220))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    elif magnet == LHCStatusOptions.EXPMagnets.LHCb_dipole:
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhcbds.png")
        rgb_img = img.convert('RGB')
        if Color(*rgb_img.getpixel((365,260))).g == 255:
            print("{} is functioning correctly.".format(magnet.name.replace('_',' ')))
        else:
            print("{} is faulty.".format(magnet.name.replace('_', ' ')))
    else:
        pass