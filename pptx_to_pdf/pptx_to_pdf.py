import os
import win32com.client

ppttoPDF = 32

current_dir = os.getcwd() # Get current dir
directory = os.fsencode(current_dir)
fil = os.listdir(directory)


print(f'{current_dir=}')
print(f'{directory=}')
print(f'{fil=}')

for root, dirs, files in os.walk(r'.', topdown=False):
    if dirs == ['INP']:
        for f in files:
            print(f)

            if f.endswith(".pptx"):
                try:
                    print(f)
                    in_file=os.path.join(root,f)
                    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                    deck = powerpoint.Presentations.Open(in_file)
                    deck.SaveAs(os.path.join(root,f[:-5]), ppttoPDF) # formatType = 32 for ppt to pdf
                    deck.Close()
                    powerpoint.Quit()
                    print('done')
                    pass
                except:
                    print('could not open')
                    # os.remove(os.path.join(root,f))
            elif f.endswith(".ppt"):
                try:
                    print(f)
                    in_file=os.path.join(root,f)
                    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                    deck = powerpoint.Presentations.Open(in_file)
                    deck.SaveAs(os.path.join(root,f[:-4]), ppttoPDF) # formatType = 32 for ppt to pdf
                    deck.Close()
                    powerpoint.Quit()
                    print('done')
                    pass
                except:
                    print('could not open')
                    # os.remove(os.path.join(root,f))
            else:
                pass

