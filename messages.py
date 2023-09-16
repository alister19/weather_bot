from api_service import get_weather
from coordinates import get_coordinates


def weather() -> str:
    wthr = get_weather(get_coordinates())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Температура {wthr.temperature}°C, ощущается {wthr.temperature_feeling}°C'

def wind() -> str:
    wthr = get_weather(get_coordinates())
    return f'{wthr.wind_direction} ветер {wthr.wind_speed} м/с'

def sun_time() -> str:
    wthr = get_weather(get_coordinates())
    return f'Восход солнца: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Заход солнца: {wthr.sunset.strftime("%H:%M")}\n'