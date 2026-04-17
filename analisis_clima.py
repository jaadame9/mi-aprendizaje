temperaturas = [12,23,45,35,26,27,24,25,22,26,24]

suma_total=sum(temperaturas)
promedio=suma_total/len(temperaturas)

maxima= max(temperaturas)

if maxima> 35:
	print(f"El promedio de esta semana fue: {maxima}°C")
else:
	print(f"La temperatura más alta fue: {maxima}°C")
