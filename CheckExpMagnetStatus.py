from Web import getImage
from Color import Color

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