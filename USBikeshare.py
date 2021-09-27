import time
import pandas as pd
import numpy as np

CHICAGO = 'Chicago'
NYC = 'New York City'
WASHINGTON = 'Washington'

CITY_DATA = { CHICAGO: 'chicago.csv',
              NYC: 'new_york_city.csv',
              WASHINGTON: 'washington.csv' }

DAYS_OF_WEEK = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday']

MONTHS_OF_YEAR = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']

HOURS = [
    '12 AM'
    '1 AM',
    '2 AM',
    '3 AM',
    '4 AM',
    '5 AM',
    '6 AM',
    '7 AM',
    '8 AM',
    '9 AM',
    '10 AM',
    '11 AM',
    '12 PM',
    '1 PM',
    '2 PM',
    '3 PM',
    '4 PM',
    '5 PM',
    '6 PM',
    '7 PM',
    '8 PM',
    '9 PM',
    '10 PM',
    '11 PM'
]

MINUTE_SEC = 60
HOUR_SEC = 60 * MINUTE_SEC
DAY_SEC = 24 * HOUR_SEC
WEEK_SEC = 7 * DAY_SEC

# print(CITY_DATA)

START_TIME = 'Start Time'
END_TIME = 'End Time'
BIRTH_YEAR = 'Birth Year'
START_STATION = 'Start Station'
END_STATION = 'End Station'
TRIP_DURATION = 'Trip Duration'
GENDER = 'Gender'

# Added columns
START_MONTH = 'Start Month'
START_DAY_OF_WEEK = 'Start Day of Week'

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    invalid_choice = "Invalid choice..."
    ALL = 'all'

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Please enter the number of which city you would like to explore: ")
        print("1 Chicago, 2 New York City, 3 Washington")
        location = input(">")
        if location == '1':
            city = CHICAGO
            print("You chose Chicago")
            break
        elif location == '2':
            city = NYC
            print("You chose New York City")
            break
        elif location == '3':
            city = WASHINGTON
            print("You chose Washington")
            break
        else:
            print(invalid_choice)

    while True:
        get_city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
        if get_city.lower() in ('chicago', 'new york', 'washington'):
            if get_city.lower() == 'chicago':
                city_filename = chicago
            elif get_city.lower() == 'new york':
                city_filename = new_york_city
            elif get_city.lower() == 'washington':
                city_filename = washington
            break
        print('Enter a valid city name provided in the options')
    while True:
        print("Please enter the number of the (start) month you would like to explore or \"{}\": ".format(ALL))
        print("1 January ... 6 June")
        m = input(">")
        if m == ALL:
            month = None
            break
        try:
            month = int(m)
        except ValueError:
            print(invalid_choice)
            continue
        else:
            if month >= 1 and month<=6:
                print("You chose " + MONTHS_OF_YEAR[month-1])
                break
            elif month <= 12:
                print("Only January to June are in this dataset")
                print(invalid_choice)
                continue
            else:
                print(invalid_choice)
                continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("Please enter the number of the (start) day of the week that you would like to explore or \"{}\": ".format(ALL))
        print("1 Monday ... 7 Sunday")
        d = input("> ")
        if d == ALL:
            day = None
            break
        try:
            day = int(d)
        except ValueError:
            print(invalid_choice)
            continue
        else:
            if day >= 1 and day<=7:
                day -= 1
                print("You chose " + DAYS_OF_WEEK[day])
                break
            else:
                print(invalid_choice)
                continue

    print_divider()
    return city, month, day        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month is None, day is None)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        trip_length_time_of_day_correlation(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Bye!")
            break


if __name__ == "__main__":
    main()    