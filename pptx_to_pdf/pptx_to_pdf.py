import os
import win32com.client

ppttoPDF = 32

current_dir = os.getcwd()  # Get current dir

print(f"{current_dir=}")

for root, dirs, files in os.walk(r"./pptx_to_pdf/INP/", topdown=False):
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
