import os
import sys

# Obtiene el directorio base del script actual (donde se encuentra QA)
base_dir = os.path.dirname(os.path.abspath(__file__))
# Agrega el directorio que contiene "Modules" al PATH
sys.path.append(os.path.join(base_dir, ".."))  # ".." significa el directorio padre

# Ahora podemos importar el módulo pdfAPI
from Modules.pdfDefault import main

# Lista de nombres de archivos PDF a convertir
pdf_files = ["QA/PDF/Default/06-11.pdf",    
             "QA/PDF/Default/1667243700213_980358248.pdf",                                    
             #"QA/PDF/Default/1690203601050_1994364726.pdf",                    Se cae jenkins nuevos listos
             #"QA/PDF/Default/1690808400472_1671940182.pdf",                    Se cae Jenkins nuevos listos
             #"QA/PDF/Default/Aya- WE 8.28.22.pdf",                             Se cae Jenkins nuevos listos
             #"QA/PDF/Default/Combined File.pdf",                               Se cae jenkins nuevos listos
             "QA/PDF/Default/Kronos Timecards TC 07-30-22.pdf",                 
             #"QA/PDF/Default/Scripps Approved Kronos we 6.25.22.pdf",          Se cae Jenkins nuevos listos
             #"QA/PDF/Default/Time Detail_100822-102122.pdf",                   Se cae jenkins nuevos listos
             #"QA/PDF/Default/Time Detail_July152022.pdf",                      Se cae jenkins
             "QA/PDF/Default/time weston.pdf",                                    
             "QA/PDF/Default/Default Empty.pdf",                                 
             "QA/PDF/Default/Pages 1-242 from 1690203601050_1994364726.pdf",     
             "QA/PDF/Default/Pages 243-483 from 1690203601050_1994364726-2.pdf", 
             "QA/PDF/Default/Pages 1-164 from 1690808400472_1671940182.pdf",     
             "QA/PDF/Default/Pages 165-329 from 1690808400472_1671940182.pdf",  
             "QA/PDF/Default/Pages 680-685 from Aya- WE 8.28.22.pdf",
             "QA/PDF/Default/Pages 1-100 from Combined File.pdf",
             "QA/PDF/Default/Pages 101-199 from Combined File.pdf",
             "QA/PDF/Default/Pages 1-116 from Scripps Approved Kronos we 6.25.22.pdf",
             "QA/PDF/Default/Pages 117-223 from Scripps Approved Kronos we 6.25.22.pdf",
             "QA/PDF/Default/Pages 1-24 from Time Detail_100822-102122.pdf",
             "QA/PDF/Default/Pages 26-40 from Time Detail_July152022.pdf"
             ] 


reportType = "Default"

for pdf_file in pdf_files:
    # Definir los argumentos necesarios para la función main
    response = True  # Puedes proporcionar el valor adecuado si es necesario
    
    # Llamar a la función main para convertir el PDF en Excel
    result = main(response, pdf_file, reportType, from_convert_pdf_Default=True)

    if result:
        print(f"The conversion File {pdf_file} was successful.")
    else:
        print(f"The conversion File {pdf_file} failed or no data was found.")
    
    

for pdf_file in pdf_files:
    # Definir los argumentos necesarios para la función main
    response = False  # Puedes proporcionar el valor adecuado si es necesario
    
    # Llamar a la función main para convertir el PDF en Excel
    result = main(response, pdf_file, reportType, from_convert_pdf_Default=True)

    if result:
        print(f"The conversion File {pdf_file} MINUTES was successful.")
    else:
        print(f"The conversion File {pdf_file} failed or no data was found.")