import re

def create_hyperlinks(text, links):
    for keyword, link in links.items():
        text = re.sub(r'\b' + keyword + r'\b', '<a href="' + link + '">' + keyword + '</a>', text, flags=re.IGNORECASE)
    return text

# Example usage
text = "lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eleifend, tellus at aliquet aliquam, lectus quam luctus massa, a posuere purus dui eget urna. In hac habitasse platea dictumst."
links = {
    "Lorem ipsum": "https://en.wikipedia.org/wiki/Lorem_ipsum",
    "aliquet": "https://www.dictionary.com/browse/aliquet",
    "Aenean": "https://www.dictionary.com/browse/aenean"
}

print(create_hyperlinks(text, links))
