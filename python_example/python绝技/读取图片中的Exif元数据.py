from PIL import Image
from PIL.ExifTags import TAGS


def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for tag,value in info.items():

                decoded = TAGS.get(tag,tag)
                exifData[decoded] = value
                print('info.items:', tag,decoded, value)
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print('[+]{}包含:GPS'.format(imgFileName))
            print(exifData)
    except:
        pass


if __name__ == '__main__':
    path = "C:/Users/rainb" \
           "ow/Pictures/IMG_0496.JPG"
    testForExif(path)