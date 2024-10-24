#making a list of dictionary of one's entire allocation history 
def listHistory(history): 
    d = {}
    l = []
    for i in history:
        #populating the dictionary with on record
        d["employee_id"] = i["employee_id"]
        d["vehicle_id"] = i["vehicle_id_to_allocate"]
        d["allocation_date"] = i["allocation_date"]

        #appending one record into the list
        l.append(d)
        d = {}
    return l
        
        

