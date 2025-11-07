class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherRecord:
    def __init__(self, temperature, condition, humidity):
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def __str__(self):
        return f"{self.temperature} degrees, {self.condition}, {self.humidity}% humidity"

class WeatherTracker:
    def __init__(self):
        self.records = {}

    def __str__(self):
        string = ""
        for city, weather in self.records.items():
            string += f"The weather in {city} is {weather}\n"
        return string
    
    def add_cities(self, *cities, **weather_report):
        for city in cities:
            self.update_weather(city.name, weather_report[city.name.lower()])

    def update_weather(self, city, weather_report):
        self.records[city] = WeatherRecord(temperature = weather_report["temperature"], condition = weather_report["condition"], humidity = weather_report["humidity"])
