from langchain_community.tools import DuckDuckGoSearchRun
from crewai import Agent, Task, Crew, Process
import os
from langchain_openai import ChatOpenAI
import PyPDF2
from langchain.tools import BaseTool, tool

cwd = os.getcwd()

class PdfTools():
    used_files = set()  # Keep track of used file paths

    @tool
    def pdf_tools(file_name):
        """Useful to scrape a pdf content"""
        try:
            if file_name in PdfTools.used_files:
                raise Exception("File has already been processed by PdfTools")

            pdf_file_path = os.path.join(cwd, file_name)
            print("File path:", pdf_file_path)
            with open(pdf_file_path, 'rb') as pdfFileObj:
                # Create a PDF reader object
                pdfReader = PyPDF2.PdfReader(pdfFileObj)

                # Iterate through pages 4 to 10
                text = ""
                for page_num in range(3, 7):  # Note: Page numbers are 0-indexed
                    pageObj = pdfReader.pages[page_num]
                    text += pageObj.extract_text()

            # Generate a unique temporary file path
            temp_file_path = f"temp_{file_name}.txt"

            # Write the text content to the temporary file
            with open(temp_file_path, "w", encoding=None) as temp_file:
                temp_file.write(text)

            PdfTools.used_files.add(file_name)  # Mark the file as processed
            return temp_file_path
        except Exception as e:
            print("PPPPPPPPPPPPPPPPP",str(e))
            print("The PDF file is corrupted.")
            return None