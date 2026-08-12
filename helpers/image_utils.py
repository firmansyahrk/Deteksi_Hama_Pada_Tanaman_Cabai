# utils/image_utils.py

from PIL import ExifTags

def fix_orientation(img):

    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break

        exif = dict(img._getexif().items())

        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)

        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)

        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)

    except:
        pass

    return img