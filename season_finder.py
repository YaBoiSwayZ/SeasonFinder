import requests
from geopy.geocoders import Nominatim

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_location():
    try:
        # Use an external service to get geolocation based on IP
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        if data['status'] == 'success':
            return data['lat'], data['lon'], data['country']
        else:
            return None, None, None
    except Exception as e:
        print(f"Could not determine location: {e}")
        return None, None, None

def get_season(day, month, year, hemisphere):
    # Define seasons based on the hemisphere
    if hemisphere == 'northern':
        if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day <= 19):
            return 'Winter'
        elif (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day <= 20):
            return 'Spring'
        elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 22):
            return 'Summer'
        elif (month == 9 and day >= 23) or (month in [10, 11]) or (month == 12 and day <= 20):
            return 'Autumn'
    elif hemisphere == 'southern':
        if (month == 12 and day >= 1) or (month in [1, 2]) or (month == 3 and day <= 20):
            return 'Summer'
        elif (month == 3 and day >= 21) or (month in [4, 5]) or (month == 6 and day <= 20):
            return 'Autumn'
        elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 20):
            return 'Winter'
        elif (month == 9 and day >= 21) or (month in [10, 11]) or (month == 12 and day <= 20):
            return 'Spring'
    else:
        return 'Invalid hemisphere'

    return 'Invalid date or season determination error'

def determine_hemisphere(latitude):
    if latitude > 0:
        return 'northern'
    elif latitude < 0:
        return 'southern'
    else:
        return 'equator'

# Example usage
try:
    date_input = input('Enter the date in the format dd/mm/yyyy: ')
    day, month, year = map(int, date_input.split('/'))
    
    latitude, longitude, country = get_location()
    
    if latitude is not None:
        hemisphere = determine_hemisphere(latitude)
        season = get_season(day, month, year, hemisphere)
        print(f"Detected Location: {country}")
        print(f"Hemisphere: {hemisphere.capitalize()}")
        print(f"Season: {season}")
    else:
        print("Could not determine location, please try again.")
except ValueError:
    print('Invalid input')