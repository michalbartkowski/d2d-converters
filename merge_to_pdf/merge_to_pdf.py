import os
from PyPDF2 import PdfMerger
import win32com.client
from docx2pdf import convert
from natsort import natsorted, ns

ppttoPDF = 32

for root, dirs, files in os.walk(r"."):
    for f in files:
        print(f)

        if f.endswith(".pptx"):
            try:
                print(f)
                in_file = os.path.join(root, f)
                powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                deck = powerpoint.Presentations.Open(in_file)
                deck.SaveAs(
                    os.path.join(root, f[:-5]), ppttoPDF
                )  # formatType = 32 for ppt to pdf
                deck.Close()
                powerpoint.Quit()
                print("done")
                pass
            except:
                print("could not open")
                # os.remove(os.path.join(root,f))
        elif f.endswith(".ppt"):
            try:
                print(f)
                in_file = os.path.join(root, f)
                powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                deck = powerpoint.Presentations.Open(in_file)
                deck.SaveAs(
                    os.path.join(root, f[:-4]), ppttoPDF
                )  # formatType = 32 for ppt to pdf
                deck.Close()
                powerpoint.Quit()
                print("done")
                pass
            except:
                print("could not open")
                # os.remove(os.path.join(root,f))
        else:
            pass

for f in os.listdir("./INPUT"):
    if f.endswith(".docx") or f.endswith(".doc"):
        convert(root)
        break


merge_list = []
for file in os.listdir("./INPUT"):
    if file.endswith(".pdf"):
        merge_list.append(file)


merger = PdfMerger()
for i in natsorted(merge_list):
    merger.append("./INPUT/" + i)

merger.write("result.pdf")
merger.close()
