import openmeteo_requests
import csv
import requests_cache
import pandas as pd
from retry_requests import retry

def fetch_weather_data(lattitude, longitude, start_date, end_date, timezone):

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lattitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["apparent_temperature_max", "apparent_temperature_min", "apparent_temperature_mean", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": timezone
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_apparent_temperature_max = daily.Variables(0).ValuesAsNumpy()
    daily_apparent_temperature_min = daily.Variables(1).ValuesAsNumpy()
    daily_apparent_temperature_mean = daily.Variables(2).ValuesAsNumpy()
    daily_sunrise = daily.Variables(3).ValuesAsNumpy()
    daily_sunset = daily.Variables(4).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(5).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(6).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(7).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(8).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(9).ValuesAsNumpy()
    daily_precipitation_hours = daily.Variables(10).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(11).ValuesAsNumpy()
    daily_wind_gusts_10m_max = daily.Variables(12).ValuesAsNumpy()
    daily_wind_direction_10m_dominant = daily.Variables(13).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["apparent_temperature_max"] = daily_apparent_temperature_max
    daily_data["apparent_temperature_min"] = daily_apparent_temperature_min
    daily_data["apparent_temperature_mean"] = daily_apparent_temperature_mean
    daily_data["sunrise"] = daily_sunrise
    daily_data["sunset"] = daily_sunset
    daily_data["daylight_duration"] = daily_daylight_duration
    daily_data["sunshine_duration"] = daily_sunshine_duration
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["precipitation_hours"] = daily_precipitation_hours
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max
    daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant


    daily_dataframe = pd.DataFrame(data = daily_data)
    return daily_dataframe

def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f"Weather data saved to {filename}")


def main(): 
    lattitude = 35.7804 # M Test Kitchen (Raleigh, NC) coordinates
    longitude = 78.7580
    timezone = "America/New_York"
    start_date = '2023-06-01'
    end_date = '2024-06-01' #year-month-day formatting
    weather_data = fetch_weather_data(lattitude, longitude, start_date, end_date, timezone)
    save_to_csv(weather_data, "weather_daily.csv")

if __name__ == "__main__":
    main()