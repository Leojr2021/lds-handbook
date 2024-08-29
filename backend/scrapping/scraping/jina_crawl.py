import requests
import os
from urls import urls
import time

def get_chapter_from_url (url):

    # Replace the path 
    url = url.replace("https://www.churchofjesuschrist.org/study/manual/general-handbook/","")
    url = url.replace("?lang=eng","")
    
    

    # Find the part that contains the number
    if '-' in url:
        return url.split('-')[0]
    else: return url
    
        
        
def create_markdown_file_from_url(url,content):
    # Extract the number from the URL
    number = get_chapter_from_url(url)
    print (content)
    if number is not None:
        # Create the filename
        filename = f"{number}.json"
        print(filename)
        # Ensure the folder exists
        folder_path = "scrapping/handbook-json"
        os.makedirs(folder_path, exist_ok=True)

    

        # Create the markdown file
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
                print("Content added.")
        except IOError as e:
            print(f"Error writing file: {e}")
            return
        except Exception as e:
            print(f"Error: {e}")
            return
        
        print(f"Json file '{filename}' created successfully!")
    else:
        print("No number found in the URL.")



# Create markdown files for each URL
for url in urls:

    while True:
        full_url = f"https://r.jina.ai/{url}"
        headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer jina_c3a698905ac14177a8ce0386e403ecb1gilY_RAbt6kafUX-n66VPz4UdrlX',
        'X-With-Links-Summary': 'true'
        }
        response = requests.get(full_url, headers=headers)


        if "Service Not Available" not in response.text and "Service Unavailable" not in response.text:
      
            try:
                create_markdown_file_from_url(url, response.text)
            except UnicodeEncodeError as e:
                print(f"UnicodeEncodeError: {e}")
            time.sleep(30)  # Wait for 30 seconds before processing the next URL
            
            break  # Exit the retry loop once successful
        else:
            print(f"Retrying for in 30 seconds...")
            time.sleep(30)  # Wait for 60 seconds before retrying
    
    