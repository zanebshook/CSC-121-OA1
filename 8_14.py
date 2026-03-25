def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car(
    'chevrolet', 'silverado', color='black', 
    drivetrain='4wd', tow_package='true')

print(car)