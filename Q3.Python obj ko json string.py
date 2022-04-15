import json


python_obj={"Name":"David", "Class":"I", "Age":6}
json_str=json.dumps(python_obj)
print(type(json_str))


