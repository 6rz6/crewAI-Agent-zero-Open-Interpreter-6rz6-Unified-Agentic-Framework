
import requests

class DuckDuckGoSearchTool():
    def duck_duck_go_search(search_term: str):
        """Performs a search using DuckDuckGo and returns a list of search results."""
        url = f'https://api.duckduckgo.com/?q={search_term}&format=json'
        response = requests.get(url)
        results = response.json().get('RelatedTopics', [])
        search_results = [result['Text'] for result in results if isinstance(result, dict) and 'Text' in result]
        return search_results
