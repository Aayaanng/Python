import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.text)

#Weather app
print("--- Weather App ---")
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# 1. Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# 2. Define API parameters (Configured for New Delhi)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 28.6214,
    "longitude": 77.2148,
    "hourly": "temperature_2m",
    "timezone": "auto",
}

# 3. Fetch data from API
try:
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
except Exception as e:
    print(f"Error fetching weather data: {e}")
    exit()

# 4. Display Location Metadata
timezone_name = response.Timezone().decode('utf-8') if isinstance(response.Timezone(), bytes) else response.Timezone()
timezone_abbr = response.TimezoneAbbreviation().decode('utf-8') if isinstance(response.TimezoneAbbreviation(), bytes) else response.TimezoneAbbreviation()

print(f"Coordinates: {response.Latitude():.4f}°N {response.Longitude():.4f}°E")
print(f"Elevation:   {response.Elevation()} m asl")
print(f"Timezone:    {timezone_name} ({timezone_abbr})")
print(f"UTC Offset:  {response.UtcOffsetSeconds()} seconds\n")

# 5. Process hourly data
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

# Generate timestamps accurately
start_dt = pd.to_datetime(hourly.Time(), unit="s", utc=True)
end_dt = pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True)
freq_delta = pd.Timedelta(seconds=hourly.Interval())

# Construct the Dataframe
hourly_data = {
    "Timestamp": pd.date_range(
        start=start_dt,
        end=end_dt,
        freq=freq_delta,
        inclusive="left"
    ).tz_convert(timezone_name)
}
hourly_data["Temperature (°C)"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data=hourly_data)

# 6. Beautiful Console Output
pd.set_option('display.max_rows', 10)  # Limits rows so your terminal isn't flooded
pd.set_option('display.width', 1000)   # Prevents text wrapping
print("Hourly Forecast:")
print(hourly_dataframe.to_string(index=False))