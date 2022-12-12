import os
import tkinter as tk
from tkinter import filedialog
import zipfile

# Create Tkinter window
root = tk.Tk()

# Create a filedialog that allows the user to select multiple files
files = filedialog.askopenfilenames(parent=root, title="Choose files to zip")

# Create a zip fi le with the selected files
with zipfile.ZipFile("files.zip", "w") as z:
    # Write each file to the zip file
    for file in files:
        z.write(file)

# Close the Tkinter window
root.destroy()
