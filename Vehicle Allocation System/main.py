from fastapi import FastAPI, HTTPException
from model import *
from config import *
from datetime import date 
from checkDate import compare_dates
from listingHistortReport import listHistory

app = FastAPI()

@app.get("/your-allication-history/{employee_id}")
def get_allocations(employee_id : int):
    history = allocations.find({"employee_id" : employee_id})
    list_history = listHistory(history)
    return list_history


#creating allocations
@app.post('/create-allocation')
def create_allocation(allocation : Allocation): 
    #gathering allocation records against the given employee_id to check if he is allowed to maken an allocation 
    employee_allocation_data = allocations.find({"employee_id" : allocation.employee_id})
    employee_allocation_data = list(employee_allocation_data)

    #gathering vehicle records to determine if the chosen vehicle is already allocated for the day or not
    vehicle_alocatted_dates = allocations.find({"vehicle_id_to_allocate" : allocation.vehicle_id_to_allocate})
    vehicle_alocatted_dates = list(vehicle_alocatted_dates)

    if len(employee_allocation_data) == 0:
        #checking if the vehicle is already booked for the day
        for i in vehicle_alocatted_dates:
            if i['vehicle_id_to_allocate'] == allocation.vehicle_id_to_allocate:
                raise HTTPException(status_code=404, detail="This vehicle is already booked for this day.Try another one.")
        else : 
            # storing today's date to compare with the given date if it is an upcoming day or not
            today = date.today()
            year, month, day = int(today.year), int(today.month), int(today.day)
            list_given_date = allocation.allocation_date.split('-')

            # comparing the dates
            date_valid_or_not = compare_dates(year, month, day, list_given_date)
            if date_valid_or_not == True:
                allocations.insert_one(dict(allocation))
            else : 
                raise HTTPException(status_code=404, detail="You have to enter an upcoming date")
        
    else: 
        #checking if the employee already allocated vehicle for the day
        for i in employee_allocation_data:
            if i["allocation_date"] == allocation.allocation_date:
                raise HTTPException(status_code=404, detail="You have already allocated for this day")
            
        else:
            #checking if the vehicle is already booked for the day
            for i in vehicle_alocatted_dates:
                if i['vehicle_id_to_allocate'] == allocation.vehicle_id_to_allocate:
                    raise HTTPException(status_code=404, detail="This vehicle is already booked for this day.Try another one.")
            else :    
                # storing today's date to compare with the given date if it is an upcoming day or not
                today = date.today()
                year, month, day = int(today.year), int(today.month), int(today.day)
                list_given_date = allocation.allocation_date.split('-')

                # comparing the dates
                date_valid_or_not = compare_dates(year, month, day, list_given_date)
                if date_valid_or_not == True:
                     allocations.insert_one(dict(allocation))
                else : 
                    raise HTTPException(status_code=404, detail="You have to enter an upcoming date")


#updating vehicles                
@app.put("/update-vehicle/{employee_id}/{allocation_date}")
def update_vehicle(employee_id : int, allocation_date : str, update : VehicleUpdate):

    #gathering allocation records against the given info to check if he is allowed to make an update
    allocation_data = allocations.find({"allocation_date" : allocation_date})

    #checking the vehicle's availability for the day
    for i in allocation_data:
        if i["vehicle_id_to_allocate"] == update.vehicle_id_to_allocate:
            return {"Error" : "This vehicle is already taken for the day"}
    #making update in case of vehicle's availability
    else:
        query_filter = {"employee_id" : employee_id}
        new_vehicle = {"$set" : {"vehicle_id_to_allocate" : update.vehicle_id_to_allocate}}
        allocations.update_one(query_filter, new_vehicle)
        return "Update Successfull!"
    
#updating dates              
@app.put("/update-date/{employee_id}/{vehicle}")
def update_date(employee_id : int, vehicle : int, update : DateUpdate):

    #gathering allocation records against the given info to check if he is allowed to make an update
    allocation_data = allocations.find({"vehicle_id_to_allocate" : vehicle})

    #checking the date's availability for the vehicle
    for i in allocation_data:
        if i["allocation_date"] == update.allocation_date:
            return {"Error" : "Make an update to the vehicle first as your given date has no availability for your vehicle"}
    #making update in case of date's availability
    else:
        # storing today's date to compare with the given date if it is an upcoming day or not
        today = date.today()
        year, month, day = int(today.year), int(today.month), int(today.day)
        list_given_date = update.allocation_date.split('-')

        # comparing the dates
        date_valid_or_not = compare_dates(year, month, day, list_given_date)
        if date_valid_or_not == True:
            query_filter = {"employee_id" : employee_id}
            new_date = {"$set" : {"allocation_date" : update.allocation_date}}
            allocations.update_one(query_filter, new_date)
            return "Update Successfull!"
        else : 
            raise HTTPException(status_code=404, detail="You have to enter an upcoming date")


#deleting allocations 
@app.delete("/delete-allocation/{employee_id}/{deletion_date}")
def delete_allocation(employee_id : int, deletion_date : str):

    # storing today's date to compare with the given date if it is an upcoming day or not
    today = date.today()
    year, month, day = int(today.year), int(today.month), int(today.day)
    list_given_date = deletion_date.split('-')

    # comparing the dates to check whether he is deleting before the date
    date_valid_or_not = compare_dates(year, month, day, list_given_date)
    if date_valid_or_not == True:
        query_filter = allocations.find_one({"employee_id": employee_id , "allocation_date" : deletion_date})    
        allocations.delete_one(query_filter)
        return "Deletion Successfull!"
    else : 
        return "You have to delete an allocation of upcoming date"









    


