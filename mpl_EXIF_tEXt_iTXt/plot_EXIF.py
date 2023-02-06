import time
from datetime import datetime

import piexif
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def add_exif(filename):
    if filename.endswith("jpg"):
        exif_dict = piexif.load(filename)
        new_date = datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        # exif_dict["0th"][piexif.ImageIFD.Make] = u'\u004D\u0069\u0063\u0068\u0061\u0142\u0020\u0042\u0061\u0072\u0074\u006B\u006F\u0077\u0073\u006B\u0069'.encode("utf8")
        exif_dict["0th"][piexif.ImageIFD.Make] = "Michal Bartkowski"
        exif_dict["0th"][piexif.ImageIFD.Software] = "matplotlib"
        exif_dict["0th"][piexif.ImageIFD.DateTime] = new_date
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_date
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_date
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filename)

    if filename.endswith("png"):
        targetImage = Image.open(filename)
        metadata = PngInfo()
        new_date = datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        metadata.add_text("Author", "Michal Bartkowski")  # tEXt png chunk
        metadata.add_text("Author", "Michał Bartkowski")  # iTXt png chunk
        metadata.add_text("Software", "matplotlib")
        metadata.add_text("Creation Time", new_date)

        targetImage.save(filename, pnginfo=metadata)
        targetImage = Image.open(filename)

        print(targetImage.text)
