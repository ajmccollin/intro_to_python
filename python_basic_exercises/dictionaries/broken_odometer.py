car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

'''car.pop('mileage')
print(car)'''

del car['mileage']
print(car)