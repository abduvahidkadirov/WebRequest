import requests as rq


r = rq.get(v_url , verify=False)
print('Content-Type: text/json')
print("")

print(r.text)

