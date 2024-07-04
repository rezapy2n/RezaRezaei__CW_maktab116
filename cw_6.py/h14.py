class URLHandler:
    @classmethod
    def parse_url(cls, url):
        
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(url)
            components = {
                "scheme": parsed_url.scheme,
                "netloc": parsed_url.netloc,
                "path": parsed_url.path,
                "params": parsed_url.params,
                "query": parsed_url.query,
                "fragment": parsed_url.fragment,
            }
            return components
        except Exception as e:
            print(f"Error parsing URL: {e}")
            return None


url_to_parse = "https://www.example.com/path/to/resource?param=value#section"
parsed_components = URLHandler.parse_url(url_to_parse)
if parsed_components:
    print("Parsed URL components:")
    for key, value in parsed_components.items():
        print(f"{key}: {value}")
else:
    print("Failed to parse the URL.")
