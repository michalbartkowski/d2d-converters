# pdf2image requires: conda install -c conda-forge poppler
import os
from pdf2image import convert_from_path

for root, dirs, files in os.walk(r"."):
    for f in files:
        print(f)

        if f.endswith(".pdf") or f.endswith(".PDF"):
            try:
                print(f)
                file = os.path.join(root, f)
                pages = convert_from_path(file, 500)
                n = 1
                for page in pages:
                    page.save(f"{f[:-4]}_{n}.jpg", "JPEG")
                    n += 1
                pass
            except:
                print("could not open")
