
import os
import pandas as pd
import requests
import json
import time
import openpyxl

final_data = []
# Parameters
#coordinates = ['18.4682,73.8363']
coordinates = input('coordinates eg. x,y ')
keywords = input('keyword for your search ')
radius = input('radius in meters ')
api_key = input('API key ') #insert your Places API key

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(coordinates)+'&radius='+str(radius)+'&keyword='+str(keywords)+'&key='+str(api_key)
i=0
while i<10:
    response = requests.get(url)
    jj = json.loads(response.text)
    results = jj['results']
    for result in results:
        name = result['name']
        place_id = result ['place_id']
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        rating = result['rating']
        types = result['types']            
        vicinity = result['vicinity']
        data = [name, place_id, lat, lng, rating, types, vicinity]
        final_data.append(data)
        #time.sleep(3)
        if 'next_page_token' not in jj:
            pass
        else:
            next_page_token = jj['next_page_token']
            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)
    i+=1
df = pd.DataFrame(final_data)
print('data collected')
df


# In[ ]:


labels = ['Name and speciality','Place ID', 'Latitude', 'Longitude', 'Ratings', 'Abouts', 'Address']
df = pd.DataFrame.from_records(final_data, columns=labels)
df1 = df.to_excel(input('excel file name ')+'.xlsx', sheet_name='sheet1')
print('Task completed....')

a = input("press Enter to exit")

