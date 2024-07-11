import re

class TextFormatter:
    def __init__(self):
        pass

    def replace_dates(self, text):
        
        date_pattern = r'\b(\d{2})/(\d{2})/(\d{4})\b'
        formatted_text = re.sub(date_pattern, r'\3-\2-\1', text)
        return formatted_text

    def find_all_urls(self, text):
       
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        return urls


if __name__ == "__main__":
    formatter = TextFormatter()
    sample_text = "Today's date is 11/07/2024. Visit https://yaboo.com for more info."
    formatted_text = formatter.replace_dates(sample_text)
    print("Formatted text:", formatted_text)
    urls = formatter.find_all_urls(sample_text)
    print("Found URLs:", urls)
