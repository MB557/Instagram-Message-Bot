from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
count = 0
counter = 0
global letter
letter = ["/"]
imageAddr = ""
imageJPG = ""

for i in range(len(file_path)):
    if (file_path[i] in letter):
        count += 1

for i in file_path:
    if (counter < count):
        imageAddr = imageAddr + i
        if(i in letter):
            counter += 1
    else:
        imageJPG = imageJPG + i