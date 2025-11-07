from gwt.modules import *

tracker = WeatherTracker()

edinburgh = City("Edinburgh", "Scotland")
glasgow = City("Glasgow", "Scotland")
munich = City("Munich", "Germany")

weather_data_edinburgh_251105 = {"temperature": 5, "condition": "Rain", "humidity": 87}
weather_data_glasgow_251105 = {"temperature": 5, "condition": "Rain", "humidity": 87}
weather_data_munich_251105 = {"temperature": 5, "condition": "Rain", "humidity": 87}

tracker.add_cities(edinburgh, glasgow, munich, edinburgh=weather_data_edinburgh_251105, glasgow=weather_data_glasgow_251105, munich=weather_data_munich_251105)
print(tracker)

weather_data_edinburgh_261105 = {"temperature": -666, "condition": "Raining Cats and Dogs", "humidity": 99.999}
tracker.update_weather(edinburgh.name, weather_data_edinburgh_261105)
print(tracker)

input("press 'enter' to continue...")
