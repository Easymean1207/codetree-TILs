from datetime import datetime

class WeatherData:
    def __init__(self, date:str, day:str, weather:str):
        self.date = date
        self.day = day
        self.weather = weather

# weather_datas안의 weather_data에서 Rain인 날의 index를 return하는 함수
def findRainIndex(weather_datas: list[WeatherData]):
    for i, weather_data in enumerate(weather_datas):
        if weather_data.weather == 'Rain':
            # return weather_data
            return i
    return None

# weather_datas안의 weather_data에서 Rain인 날을 return하는 함수
def findRain(weather_datas: list[WeatherData]):
    for i, weather_data in enumerate(weather_datas):
        if weather_data.weather == 'Rain':
            return weather_data
    return None

n = int(input())

weather_datas = []
for _ in range(n):
    given_date, given_day, given_weather = tuple(input().split())
    # 문자열 타입의 date를 datetime 형식으로 변환 & 시간 제거
    given_date = datetime.strptime(given_date, "%Y-%m-%d").date()
    # day, weather를 제일 앞글자를 대문자로
    given_day,given_weather = given_day.capitalize(), given_weather.capitalize()
    weather_datas.append(WeatherData(given_date, given_day, given_weather))

# date 순으로 자료 정렬
weather_datas.sort(key=lambda x:x.date)

rain_idx = findRainIndex(weather_datas)
print(
    weather_datas[rain_idx].date,
    weather_datas[rain_idx].day,
    weather_datas[rain_idx].weather
)

rainy = findRain(weather_datas)
# print(rainy.date, rainy.day, rainy.weather)