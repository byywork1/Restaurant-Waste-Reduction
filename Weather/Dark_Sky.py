## THIS SCRIPT IS USED FOR PIRATEWEATHER API AT SOME POINT IN THE FUTURE. 
## PIRATEWEATHER API ONLY ALLOWS HISTORICAL QUERIES MAY 2023 AND OLDER. 
## CURRENT DATA IS MUCH MORE DETAILED THAN METEO.IO

import requests
import csv
from datetime import datetime, timedelta, time
from config import pirateweather_api_key

def fetch_weather_data(api_key, latitude, longitude, current_date):
    converted_date = calculate_time_delta(current_date)
    url = f"https://timemachine.pirateweather.net/forecast/{api_key}/{latitude},{longitude},{converted_date}"
    weather_data = []
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    else: 
        print(f"API request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")
        data = 'balls'


    weather_data.append(data)

    return weather_data

def calculate_time_delta(date_str, current_time=None):
    # Parse the input date string into a datetime object
    target_date = datetime.strptime(date_str, "%m-%d-%Y")
    
    # Use the provided current_time or the current time if not provided
    if current_time is None:
        current_time = datetime.now()
    
    # Calculate the time delta (difference) in seconds
    time_delta = (target_date - current_time).total_seconds()
    
    return int(time_delta)


def save_to_csv(weather_data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'temperature', 'precipitation'])
        writer.writeheader()
        for row in weather_data:
            writer.writerow(row)

def main():
    print("starting file")
    api_key = pirateweather_api_key
    latitude = 35.7804
    longitude = 78.7580 # Raleigh, NC M Test Kitchen Coordinates
    
    # start_date = '2024-08-01'
    # end_date = '2024-08-07'

    current_date = '06-01-2023' #format must be '%m-%d-%Y'
    print('generating CSV')
    weather_data = fetch_weather_data(api_key, latitude, longitude, current_date)
    print(weather_data)
    #save_to_csv(weather_data, 'weather_data.csv')
    print('CSV generated')
    

if __name__ == "__main__":
    main()
