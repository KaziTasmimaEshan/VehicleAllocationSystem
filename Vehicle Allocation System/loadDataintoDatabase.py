from config import vehicles

dict_vehicle = {}

# inserting 1000 individual vehicle and corresponding driver info into the database collection 'vehicle'
for i in range(1,1001):
    dict_vehicle['vehicle_id'] = i
    dict_vehicle['driver_name'] = 'driver' + str(i)
    dict_vehicle['allocated_for_days'] = []

    vehicles.insert_one(dict_vehicle)
    dict_vehicle = {}
