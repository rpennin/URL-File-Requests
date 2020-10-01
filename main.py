import requests
import json

#Open the file with all the urls
file = open('input.txt','r') 

#Get a list of all the urls in the file
urls = file.read().splitlines()

#Close the file    
file.close()

#Open or create the file to save the data
file = open('output.txt', 'w')

#Loop through the urls, saving the data to the file each time
for url in urls: 
    response = requests.get(url)
    file.write(json.dumps(response.json()) + "\n")

#Close the file    
file.close()