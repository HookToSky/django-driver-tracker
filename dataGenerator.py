# import math
# from random import random, randrange
# from apscheduler.schedulers.background import BackgroundScheduler 
# from faker import Faker
# # generate fake driver profile
# def genObj(totalDrivers):
#     i = 0
#     fake = Faker()
#     o = {
#         "type": "FeatureCollection",
#         "features": []
#     }
#     # file = open('drivers.get.json', 'w+')
#     # file.write(json.dumps(o))
    
#     while i < totalDrivers:
#         d = {
#             "type": "Feature",
#             "geometry": {
#                 "type": "Point",
#                 "coordinates": [float(fake.longitude()), float(fake.latitude())],
#             },
#             "properties": {
#                 "driverName": fake.name(),
#                 "driverCityOrigin": fake.city(),
#                 "driverLanguage": ['de', 'en', 'nl', 'fr', 'es', 'ar'][randrange(6)],
#                 "driverPhone": fake.phone_number(),
#                 'driverInfo': fake.catch_phrase(),
#                 "licensePlate": fake.license_plate(),
#                 "kmDriven": int(random() * 100000),
#             },
#         }
#         o["features"].append(d)
#         i = i+1
#     # file2 = open("./drivers.get.json", "w")
#     # file2.write(json.dumps(o))
#     # pickle.dump(o, open("drivers.pkl", "wb"))

#     return o


# # generate 10 fake drivers
# driver_geojson = genObj(10)

# sched = BackgroundScheduler()
# # TODO randomly update driver location every 5 seconds
# def updatePositions(x0, y0):
#     radiusInDegrees = 10000 / 111000 # radius is 10km
#     u = random()
#     v = random()
#     w = radiusInDegrees * math.sqrt(u)
#     t = 2 * math.pi * v
#     x = w * math.cos(t)
#     y = w * math.sin(t)

#     new_x = x / math.cos(math.radians(y0))
#     new_longitude = new_x + x0
#     new_latitude = y + y0
#     return {new_latitude, new_longitude}

# def updateDrivers():
#     global driver_geojson
#     drivers = driver_geojson["features"]
#     for idx, driver in enumerate(drivers):
#         current_location = driver["geometry"]["coordinates"]
#         new_latitude, new_longitude = updatePositions(current_location[0], current_location[1])
#         driver_geojson["features"][idx]["geometry"]["coordinates"] = [float(new_longitude), float(new_latitude)]
#         print('old:', current_location,"id:", idx, "- updated:", driver_geojson["features"][idx]["geometry"]["coordinates"])

# def getDrivers():
#     return driver_geojson


# sched.add_job(updateDrivers, 'interval', seconds = 5)
# sched.start()