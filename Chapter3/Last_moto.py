motorcycles = ['honda', 'suzuki', 'triumph', 'tomos']
print(motorcycles)

last_moto = motorcycles.pop()
print("My last motorcycle was a " + last_moto.title() + " m'focker.")
last_moto = motorcycles
print(last_moto)

print(motorcycles)
print(last_moto)
motorcycles = motorcycles.remove('suzuki')
print(motorcycles)
print(last_moto)
