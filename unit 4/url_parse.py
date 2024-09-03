from urllib.parse import urlparse

def parse_url(url):
   
   
        parsed_url = urlparse(url)
        
      
        print(f"Scheme: {parsed_url.scheme}")
        print(f"Netloc: {parsed_url.netloc}")
        print(f"Path: {parsed_url.path}")
        print(f"Params: {parsed_url.params}")
        print(f"Query: {parsed_url.query}")
        print(f"Fragment: {parsed_url.fragment}")
   


url = "https://medium.com/bancolombia-tech/flutter-provider-what-is-it-what-is-it-for-and-how-to-use-it-47d6941860d7"


parse_url(url)
