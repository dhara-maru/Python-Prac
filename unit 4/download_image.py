import requests

def download_image(url, output_file):
    
        response = requests.get(url)
        
        if response.status_code == 200:
           
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved to {output_file}")
        else:
            print(f"Error: Unable to download the image. Status code: {response.status_code}")
  

image_url = "https://raw.githubusercontent.com/rrousselGit/provider/master/resources/flutter_favorite.png"
output_file = "downloaded_image.jpg"

download_image(image_url, output_file)
