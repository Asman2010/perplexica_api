# Perplexica API
This project provides a Python API for interacting with Perplexica, an advanced internet searching agent and a great opensource alternative of Perplexity.

## Important Note
**This API requires Perplexica version 1.8.0 or higher.**

Please ensure you have the correct version of Perplexica installed before using this API.

## Features
- Automated query submission to Perplexica
- Efficient result retrieval and processing
- Built-in error handling and retry logic
- Headless browser automation using Selenium

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/your-username/perplexica-api.git
   cd perplexica-api
   ```

2. Install the required packages:
   ```
   pip install selenium requests
   ```

3. Ensure you have Chrome and ChromeDriver installed for Selenium to work properly.

## Usage
Here's a basic example of how to use the Perplexica API. You can find the code file in examples directory:

```python
from search_api import InternetSearch

# Create a new search instance
search = InternetSearch("Who created Apple")

# Perform the search
print("Submitting query to Perplexica...")
search.search()

# Retrieve and process the results
print("Processing results...")
result = search.process()

if result:
    print("Search result:")
    print(result)
else:
    print("Failed to retrieve search result.")
```

## Configuration
You may need to adjust the following constants in `search_api.py` to match your Perplexica setup:

- `BASE_URL`: The base URL for Perplexica queries
- `API_URL`: The API endpoint for retrieving chat information
- `WAIT_TIME`: Time to wait between result checks
- `MAX_RETRIES`: Maximum number of retry attempts

## Error Handling
The API includes basic error handling for common issues such as network problems or unexpected responses. Check the console output for error messages if you encounter any issues.

## Contributing
Contributions to improve the Perplexica API are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This API is not officially associated with Perplexica.
