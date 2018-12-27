from Web import getImage
from Color import Color

def Check60AmpPCPermit():
    colors = list()
    img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
    rgb_img = img.convert('RGB')
    colors.append(Color(*rgb_img.getpixel((108,403))))   #S12
    colors.append(Color(*rgb_img.getpixel((203,403))))   #S23
    colors.append(Color(*rgb_img.getpixel((297,403))))   #S34
    colors.append(Color(*rgb_img.getpixel((392,402))))   #S45
    colors.append(Color(*rgb_img.getpixel((498,402))))   #S56
    colors.append(Color(*rgb_img.getpixel((595,402))))   #S67
    colors.append(Color(*rgb_img.getpixel((688,403))))   #S78
    colors.append(Color(*rgb_img.getpixel((772,402))))   #S81

    for color in colors:
        if color.r == 255:
            print("A PCPermit is down.")
            return
    print("All PCPermits are up.")

def Check60AmpPCPermitIndividual():
    print("Which PC Permit do you want to check?")
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
            GetPCPermitStatusIndividual("Sector 12")
        elif int(selection) == 2:
            GetPCPermitStatusIndividual("Sector 23")
        elif int(selection) == 3:
            GetPCPermitStatusIndividual("Sector 34")
        elif int(selection) == 4:
            GetPCPermitStatusIndividual("Sector 45")
        elif int(selection) == 5:
            GetPCPermitStatusIndividual("Sector 56")
        elif int(selection) == 6:
            GetPCPermitStatusIndividual("Sector 67")
        elif int(selection) == 7:
            GetPCPermitStatusIndividual("Sector 78")
        elif int(selection) == 8:
            GetPCPermitStatusIndividual("Sector 81")
        else:
            pass

def GetPCPermitStatusIndividual(Sector):
    if Sector == "Sector 12":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((108,403)))   #S12
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 23":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((203,403)))   #S23
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 34":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((297,403)))   #S34
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 45":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((392,402)))   #S45
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 56":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((498,402)))   #S56
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 67":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((595,402)))   #S67
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 78":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((688,403)))   #S78
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    elif Sector == "Sector 81":
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        C = Color(*rgb_img.getpixel((772,402)))   #S81
        if C.r == 255:
            print("The PCPermit is down.")
            return
        print("The PCPermit is up.")
    else:
        pass