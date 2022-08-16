employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def id_name(employee_list):
    id = employee_list['id']
    names = employee_list["name"]
    return [id,names]

id_no = []
names = []
for person in map( id_name, employee_list):
    id_no.append(person[0])
    names.append(person[1][0])

employee_dict = {key : value for (key, value) in zip(names, id_no)}
print(employee_dict)

