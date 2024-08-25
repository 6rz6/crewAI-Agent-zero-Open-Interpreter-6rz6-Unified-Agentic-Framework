import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
import PyPDF2
import os
cwd = os.getcwd()

class PDFTools():
  @tool("Scraper Tool")
  def pdf_tools(file_name: str):
        """Useful to scrape a pdf content"""
        try:
            pdf_file_path = os.path.join(cwd, file_name)
            print("\n\n\n\n KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", pdf_file_path)
            with open(pdf_file_path, 'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfReader(pdfFileObj)

                text = ""
                for page_num in range(3, 7):  # Note: Page numbers are 0-indexed
                    pageObj = pdfReader.pages[page_num]
                    text += pageObj.extract_text()
            print("EEEEEEEEEEEEEEEEEE",len(text))
                 
            return text
        except Exception as e:
            print("PPPPPPPPPPPPPPPPP",str(e))
            print("The PDF file is corrupted.")
            return None
