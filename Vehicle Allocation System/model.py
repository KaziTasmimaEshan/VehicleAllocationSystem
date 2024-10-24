from pydantic import BaseModel
from typing import Optional

class Vehicle(BaseModel):
    vehicle_id : int    
    driver_name : str
    allocated_for_days : list

class Allocation(BaseModel):
    employee_id : int
    vehicle_id_to_allocate : int
    allocation_date : str

class VehicleUpdate(BaseModel):
    vehicle_id_to_allocate : int

class DateUpdate(BaseModel):
    allocation_date: str



    



