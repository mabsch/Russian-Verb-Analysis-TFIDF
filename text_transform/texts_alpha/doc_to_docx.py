import os
import re
import win32com.client as win32
from win32com.client import constants

# Directory containing .doc files
directory = r'C:\Users\Angel\Dropbox\My PC (UNC-PF2A4YMK)\Documents\Capstone\frequency_list\text_transform\texts_alpha\class\docs'

def save_as_docx(file):
    try:
        # Opening MS Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(file)
        doc.Activate()

        # Rename path with .docx
        new_file_abs = os.path.abspath(file)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)
        print(f"Converted {file} to .docx successfully.")
    except Exception as e:
        print(f"Error converting {file}: {e}")

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.doc'):
        file_path = os.path.join(directory, filename)
        save_as_docx(file_path)
