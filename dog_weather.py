import requests
import json
from datetime import datetime

weather_url = "https://home.openweathermap.org/"

import weather_secret
weather_key = weather_secret.weather_key
latitude = weather_secret.latitude
longitude = weather_secret.longitude

weather_api = f"http://api.openweathermap.org/data/2.5/weather?lon={longitude}&lat={latitude}&APPID={weather_key}"
forecast_api = f"http://api.openweathermap.org/data/2.5/forecast?lon={longitude}&lat={latitude}&APPID={weather_key}"
curfore_api = f"https://api.openweathermap.org/data/2.5/onecall?lon={longitude}&lat={latitude}&exclude=daily,alerts&appid={weather_key}&units=imperial"

def get_weather_data():
    r = requests.get(curfore_api).json()

    minute_array = []
    for minute in r['minutely']:
        if minute["precipitation"] > 0:
            ts = datetime.strftime(datetime.fromtimestamp(minute['dt']), "%H:%M")
            pc = minute["precipitation"]
            minute_array.append({"time": ts, "pct": pc})

    day_dict = {}

    if minute_array:
        min_precip_start = minute_array[0]['time']
        min_precip_start_pct = minute_array[0]['pct']
        min_precip_ends = minute_array[-1]['time']
        min_precip_ends_pct = minute_array[-1]['pct']
        minute_forecast = f"Rain may start around {min_precip_start} (@precip {min_precip_start_pct}%) and end around {min_precip_ends} (@precip {min_precip_ends_pct}%)."
    else:
        minute_forecast = "No precipitation for the next hour"

    day_dict["minutes"] = minute_forecast

    # print(f"Minute forecast @60m: {minute_forecast}\n")
    # print("Hourly forecast for the next 36 hours:")

    day_list = []
    index = 0
    for hour in r['hourly']:
        ts = int(datetime.strftime(datetime.fromtimestamp(hour['dt']), "%H"))
        ts_full = datetime.strftime(datetime.fromtimestamp(hour['dt']), "%a %m/%d %-I%p")
        ts_hour = datetime.strftime(datetime.fromtimestamp(hour['dt']), "%-I%p")
        ds = datetime.strftime(datetime.fromtimestamp(hour['dt']), "%m-%d")
        weather_main = hour['weather'][0]['main']
        weather_desc = hour['weather'][0]['description']
        weather_temp = hour['temp']
        rain_prob_pct = float(hour['pop'])

        # if not day_list:
        #     day_list.append({ds: [{"morning_walks": []},{"midday_walks": []},{"nightly_walks": []}]})


        if ds not in day_dict:
            # print('Adding the following dictionary to the day_list: {ds: [{"morning_walks": []},{"midday_walks": []},{"night_walks": []}]}')
            day_dict[ds] = [{"morning_walks": []},{"midday_walks": []},{"night_walks": []}]

        if 7 <= ts <= 10:
            if rain_prob_pct > 0.01:
                phrase = f"Chance of rain: {int(rain_prob_pct * 100)}% ({weather_temp}°)"
            else:
                phrase = f"No rain ({weather_desc}) @ {weather_temp}°"
            entry = {'time': ts_hour, 'desc': phrase}
            day_dict[ds][0]['morning_walks'].append(entry)

        if 15 <= ts <= 18:
            if rain_prob_pct > 0.01:
                phrase = f"Chance of rain: {int(rain_prob_pct * 100)}% ({weather_temp}°)"
            else:
                phrase = f"No rain ({weather_desc}) @ {weather_temp}°"
            entry = {'time': ts_hour, 'desc': phrase}
            day_dict[ds][1]['midday_walks'].append(entry)

        if 21 <= ts <= 24:
            if rain_prob_pct > 0.01:
                phrase = f"Chance of rain: {int(rain_prob_pct * 100)}% ({weather_temp}°)"
            else:
                phrase = f"No rain ({weather_desc}) @ {weather_temp}°"
            entry = {'time': ts_hour, 'desc': phrase}
            day_dict[ds][2]['night_walks'].append(entry)

        index += 1
        # Get only 36 hours of data.
        if index == 36:
            break

    return day_dict

# print(json.dumps(day_dict))
# for day in day_dict.items():
#     print(f"{day[0]}:")

#     if day[1][0]['morning_walks']:
#         print("  Morning walks:")
#         for i,walk in enumerate(day[1][0]['morning_walks']):
#             print(f"  {day[1][0]['morning_walks'][i]['time']} - {day[1][0]['morning_walks'][i]['desc']}")
#         print()

#     if day[1][1]['midday_walks']:
#         print("  Mid-day walks:")
#         for i,walk in enumerate(day[1][1]['midday_walks']):
#             print(f"  {day[1][1]['midday_walks'][i]['time']} - {day[1][1]['midday_walks'][i]['desc']}")
#         print()

#     if day[1][2]['night_walks']:
#         print("  Night walks:")
#         for i,walk in enumerate(day[1][2]['night_walks']):
#             print(f"  {day[1][2]['night_walks'][i]['time']} - {day[1][2]['night_walks'][i]['desc']}")
#         print()


if __name__ == "__main__":
    print(json.dumps(get_weather_data()))
    