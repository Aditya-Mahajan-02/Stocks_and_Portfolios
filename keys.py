
# Function call to get url and keys
# will return a list [Publickey, Name, URL]
def GetKeys():
    public = 'o4GUN1bkIRJWjhmzUibnbo7RekNvspAs'
    name = 'Working'
    url = f'https://api.polygon.io/v1/open-close/{name}/2023-10-16?apiKey={public}'
    return [public, name, url]


