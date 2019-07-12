import pyowm
 
apikey = 'fb1b71f0612d663b1b0af5a8904b8f09'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()


wind = w.get_wind()
w.get_humidity()
humidity =w.get_humidity()
print(wind)
print(humidity)

import pyowm
 
apikey = 'fb1b71f0612d663b1b0af5a8904b8f09'
owm = pyowm.OWM(apikey)
observation = owm.rain_at_place('Hong kong, China')
w = observation.get_rain()


wind = w.get_wind()
w.get_humidity()
tempreture = w.get_tempreture()
presh=w.get_pressure()
clud=w.get_clouds()
ran=w.get_rain()
snow=w.get_snow()

print(wind)
print(humidity)
print(tempreture)
print(pressure)
print(clouds)
print(rian)
print(snow)