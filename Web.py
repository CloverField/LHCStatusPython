from PIL import Image
import requests
from io import BytesIO

def getImage(url):
    responce = requests.get(url)
    img = Image.open(BytesIO(responce.content))
    return img