import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

class UrlsTool():
  @tool("Scraper Tool")
  def url_tools(url: str):
    "Useful tool to scrap a website content, use to learn more about a given url."

    print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    print(text)
    return text
   
        
        
