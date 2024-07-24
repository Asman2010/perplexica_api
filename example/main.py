from search_api import InternetSearch

def main():
    query = "Who created Apple"
    search = InternetSearch(query)

    print("Performing search...")
    search.search()

    print("Processing results...")
    result = search.process()
    
    if result:
        print("Search result:")
        print(result)
    else:
        print("Failed to retrieve search result.")

if __name__ == "__main__":
    main()
  
