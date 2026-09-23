aantal_tjirps_per_minuut = int(input())

temp_fahrenheit = 50 + ((aantal_tjirps_per_minuut - 40) / 4)
temp_celsius = 10 + ((aantal_tjirps_per_minuut - 40) / 7)

print("temperatuur (Fahrenheit):", temp_fahrenheit)
print("temperatuur (Celsius):", temp_celsius)
