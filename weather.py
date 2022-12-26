import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=41.8781&lon=87.629&appid=c29e9c84dbe9df8e565759dee9a4ede4")

response_json = (response.json())

temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"]

class City:
    def __init__(self,name,lat,long,unit):
        self.name = name
        self.lat = lat
        self.long = long
        self.unit = unit
        self.get_data()

    def get_data(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.unit}&lat={self.lat}&lon={self.long}&appid=c29e9c84dbe9df8e565759dee9a4ede4")

        self.response_json = (response.json())
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        if self.unit == "Imperial":
            print(f"In {self.name}, it is currently {self.temp} degrees fahrenheit")
            print(f"The high today is: {self.temp_max}")
            print(f"The low today is: {self.temp_min}")
        else:
            print(f"In {self.name}, it is currently {self.temp} degrees celsius")
            print(f"The high today is: {self.temp_max}")
            print(f"The low today is: {self.temp_min}")

dream_city = City("San Francisco", 37.773972, -122.431297, "Imperial")
vacation_city = City("Austin", 30.266666, -97.733330, "Metric")
my_city = City("Chicago",  41.881832, -87.623177, "Imperial")


dream_city.temp_print()
vacation_city.temp_print()
my_city.temp_print()