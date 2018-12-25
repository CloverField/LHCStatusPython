from Web import getImage

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
        else:
            pass

def GetSectorStatus(Sector):

    if Sector == "Sector 12":
        pixels = list()
        img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc2.png")
        rgb_img = img.convert('RGB')
        pixels.append(rgb_img.getpixel((100,100)))
        pixels.append(rgb_img.getpixel((188,100)))
        pixels.append(rgb_img.getpixel((288,100)))
        pixels.append(rgb_img.getpixel((378,100)))
        pixels.append(rgb_img.getpixel((478,100)))
        pixels.append(rgb_img.getpixel((568,100)))
        pixels.append(rgb_img.getpixel((668,100)))
        pixels.append(rgb_img.getpixel((758,100)))
        pixels.append(rgb_img.getpixel((858,100)))
        pixels.append(rgb_img.getpixel((948,100)))

        for pixel in pixels:
            if pixel[0] == 255:
                print("Looks like Cryo is down in Sector 12.")
                return

        print("Everything looks good in Sector 12")

    elif Sector == "Sector 23":
        pass
