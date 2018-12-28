from PIL import Image
import pytesseract
from Web import getImage

def CheckVistarPage():
    img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
    print(pytesseract.image_to_string(img))

def CheckVistarComments():
    img = getImage("https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png")
    print(pytesseract.image_to_string(img.crop((0,556,512,731))))