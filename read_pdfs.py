
#This file pulls all of the pdfs in 2019 questionnaire and organizes the data

import os

my_dir='2019_Questionnaires'


def extract_text(filename):
  import PyPDF2
  text = ""
  with open(my_dir+ "/" + filename,'rb') as PDF_file:
    pdf_object = PyPDF2.PdfFileReader(PDF_file)
    for page in range(pdf_object.numPages):
      text+=pdf_object.getPage(page).extractText()
  return text




for filename in os.listdir(my_dir):
  print(extract_text(filename).replace('\n',''))