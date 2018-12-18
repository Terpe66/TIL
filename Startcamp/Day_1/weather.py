from darksky import forecast

multicampus = forecast('6679325f16305778e892f8c97aa318de', 37.501494, 127.039638)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])
