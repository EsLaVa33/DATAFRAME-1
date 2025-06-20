import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
archivo_excel = askopenfilename(
    title="Selecciona un archivo Excel",
    filetypes=[("Archivos Excel", "*.xlsx *.xls"), 
               ("Todos los archivos", "*.*")])

if archivo_excel:
    df = pd.read_excel(archivo_excel)
    print("Archivo cargado correctamente:")
    print(df.head())
else:
    print("No se seleccionó ningún archivo")
