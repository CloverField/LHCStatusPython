from Web import getImage
from Color import Color

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
        colors.append(Color(*rgb_img.getpixel((100,100))))  #CMITR1
        colors.append(Color(*rgb_img.getpixel((188,100))))  #CSITR1
        colors.append(Color(*rgb_img.getpixel((288,100))))  #CMMSR1
        colors.append(Color(*rgb_img.getpixel((378,100))))  #CSMSR1
        colors.append(Color(*rgb_img.getpixel((478,100))))  #CMAR12
        colors.append(Color(*rgb_img.getpixel((568,100))))  #CSAR12
        colors.append(Color(*rgb_img.getpixel((668,100))))  #CMMSL2
        colors.append(Color(*rgb_img.getpixel((758,100))))  #CSMSL2
        colors.append(Color(*rgb_img.getpixel((858,100))))  #CMITL2
        colors.append(Color(*rgb_img.getpixel((948,100))))  #CSITL2

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 12.")
                return
        print("Everything looks good in Sector 12.")

    elif Sector == "Sector 23":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((100,140))))  #CMITR2
        colors.append(Color(*rgb_img.getpixel((188,140))))  #CSITR2
        colors.append(Color(*rgb_img.getpixel((288,140))))  #CMMSR2
        colors.append(Color(*rgb_img.getpixel((378,140))))  #CSMSR2
        colors.append(Color(*rgb_img.getpixel((478,140))))  #CMAML3
        colors.append(Color(*rgb_img.getpixel((568,140))))  #CSAML3

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 23.")
                return
        print("Everything looks good in Sector 23.")

    elif Sector == "Sector 34":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((478,175))))  #CMAML3
        colors.append(Color(*rgb_img.getpixel((568,175))))  #CSAML3
        colors.append(Color(*rgb_img.getpixel((668,175))))  #CMMSL1
        colors.append(Color(*rgb_img.getpixel((758,175))))  #CSMSL1

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 34.")
                return
        print("Everything looks good in Sector 34.")

    elif Sector == "Sector 45":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((288,210))))  #CMMSR4
        colors.append(Color(*rgb_img.getpixel((378,210))))  #CSMSR4
        colors.append(Color(*rgb_img.getpixel((478,210))))  #CMAR45
        colors.append(Color(*rgb_img.getpixel((568,210))))  #CSAR45
        colors.append(Color(*rgb_img.getpixel((668,210))))  #CMMSL5
        colors.append(Color(*rgb_img.getpixel((758,210))))  #CSMSL5
        colors.append(Color(*rgb_img.getpixel((858,210))))  #CMITL6
        colors.append(Color(*rgb_img.getpixel((948,210))))  #CSITL6

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 45.")
                return
        print("Everything looks good in Sector 45.")

    elif Sector == "Sector 56":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((100,245)))) #CMITR5
        colors.append(Color(*rgb_img.getpixel((188,245)))) #CSITR5
        colors.append(Color(*rgb_img.getpixel((288,245)))) #CMMSR5
        colors.append(Color(*rgb_img.getpixel((378,245)))) #CSMSR5
        colors.append(Color(*rgb_img.getpixel((478,245)))) #CMAR56
        colors.append(Color(*rgb_img.getpixel((568,245)))) #CSAR56
        colors.append(Color(*rgb_img.getpixel((668,245)))) #CMMSL6
        colors.append(Color(*rgb_img.getpixel((758,245)))) #CSMSL6

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 56.")
                return
        print("Everything looks good in Sector 56.")

    elif Sector == "Sector 67":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((288,280))))  #CMMSR6
        colors.append(Color(*rgb_img.getpixel((378,280))))  #CSMSR6
        colors.append(Color(*rgb_img.getpixel((478,280))))  #CMAML7
        colors.append(Color(*rgb_img.getpixel((568,280))))  #CSAML7

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 67.")
                return
        print("Everything looks good in Sector 67.")

    elif Sector == "Sector 78":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((478,315))))  #CMAMR7
        colors.append(Color(*rgb_img.getpixel((568,315))))  #CSAMR7
        colors.append(Color(*rgb_img.getpixel((668,315))))  #CMMSL8
        colors.append(Color(*rgb_img.getpixel((758,315))))  #CSMSL8
        colors.append(Color(*rgb_img.getpixel((858,315))))  #CMITL8
        colors.append(Color(*rgb_img.getpixel((948,315))))  #CSITL8

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 78.")
                return
        print("Everything looks good in Sector 78.")

    elif Sector == "Sector 81":
        colors = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        colors.append(Color(*rgb_img.getpixel((100,350))))  #CMITR8
        colors.append(Color(*rgb_img.getpixel((188,350))))  #CSITR8
        colors.append(Color(*rgb_img.getpixel((288,350))))  #CMMSR8
        colors.append(Color(*rgb_img.getpixel((378,350))))  #CSMSR8
        colors.append(Color(*rgb_img.getpixel((478,350))))  #CMAR81
        colors.append(Color(*rgb_img.getpixel((568,350))))  #CSAR81
        colors.append(Color(*rgb_img.getpixel((668,350))))  #CMMSL1
        colors.append(Color(*rgb_img.getpixel((758,350))))  #CSMSL1
        colors.append(Color(*rgb_img.getpixel((858,350))))  #CMITL1
        colors.append(Color(*rgb_img.getpixel((948,350))))  #CSITL1

        for color in colors:
            if color.r == 255:
                print("Looks like Cryo is down in Sector 81.")
                return
        print("Everything looks good in Sector 81.")