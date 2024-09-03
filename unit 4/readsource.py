import requests

def read_webpage_source(url):
 
       
        response = requests.get(url)
        
        if response.status_code == 200:
            # Print the source code of the webpage
            print(response.text)
        else:
            print(f"Error: Unable to retrieve the webpage. Status code: {response.status_code}")
   

webpage_url = "https://pub.dev/packages/provider"

read_webpage_source(webpage_url)
