import requests
with open('api.txt') as f: API_KEY,SEARCH_ENGINE_ID = f.read().splitlines()
def google_search(query, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return response.json()
def main():
    query = input("Enter your search query: ")
    results = google_search(query, API_KEY, SEARCH_ENGINE_ID)
    
    if 'items' in results:
        print(f"\nTop 10 results for '{query}':\n")
        for i, item in enumerate(results['items'], 1):
            print(f"{i}. {item['title']}")
            print(f"   URL: {item['link']}")
            print(f"   Snippet: {item['snippet']}\n")
if __name__ == "__main__":
    main()