import requests as rq
import json
import req_ini as vals

r = rq.get(vals.v_url , verify=False)

print("++++++")

json_string = json.dumps(r.text)
print(json_string)

json_data = json.loads(json_string)

print("++++++")
print(json_data)



#print("Name: ", vals.get_name)
