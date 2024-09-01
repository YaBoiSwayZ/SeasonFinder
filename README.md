SeasonFinder determines the season based on a given date and the user's geographical location. The script uses an external service to identify the user's location and then calculates the corresponding season based on the hemisphere they reside in.

## Features

- **Automatic Location Detection**: The script automatically determines the user's latitude, longitude, and country using the `ip-api.com` service.
- **Hemisphere Detection**: Based on the detected latitude, the script identifies whether the user is in the Northern or Southern Hemisphere.
- **Season Calculation**: The script calculates the current season based on the provided date and the detected hemisphere.

## Prerequisites

Before running the script, make sure you have the following Python packages installed:

- `requests`: Used to make HTTP requests to the location API.
- `geopy`: Used for geographical calculations (though in this script, only `Nominatim` is imported but not used).

You can install the required packages using pip:

```
pip install requests geopy
```

## Usage

1. **Run the Script**: Execute the script using Python in your terminal or command prompt.

```
python season_finder.py
```

2. **Input the Date**: When prompted, enter the date in the format `dd/mm/yyyy`.

3. **View Results**: The script will automatically detect your location, determine the hemisphere, and display the corresponding season for the provided date.

### Example

```
Enter the date in the format dd/mm/yyyy: 15/09/2023
Detected Location: Australia
Hemisphere: Southern
Season: Spring
```

## Limitations

- **Location Accuracy**: The script relies on IP-based geolocation, which may not always be accurate.
- **Hemisphere Coverage**: The script is designed primarily for users in the Northern and Southern Hemispheres. Users located at the equator may receive an "Invalid hemisphere" message.
- **Date Validity**: The script does basic validation on the date input but does not account for all edge cases, such as non-existent dates.

## Future Improvements

- **Support for Manual Location Input**: Add the option to manually input location details for better accuracy.
- **Enhanced Date Validation**: Improve date validation to handle more edge cases and provide more informative error messages.

## License

This project is licensed under the MIT License.
