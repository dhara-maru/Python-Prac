import requests

def download_webpage(url, output_file):
   
        response = requests.get(url)
        
        if response.status_code == 200:
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Webpage downloaded and saved to {output_file}")
        else:
            print(f"Error: Unable to download the webpage. Status code: {response.status_code}")
   

webpage_url = "https://www.geeksforgeeks.org/flutter-provider-package/"
output_file = "downloaded_webpage.html"

download_webpage(webpage_url, output_file)
