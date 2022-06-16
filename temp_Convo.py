farenheit_temp = 45
celsius_temp = 11

fToCelsius = (farenheit_temp-32) * (5/9)
cToFarenheit = (celsius_temp * 9 / 5) + 32

print("%f f in Celsius: %f" %(farenheit_temp, fToCelsius))
print("%f c in Farenheit: %f" %(celsius_temp, cToFarenheit))