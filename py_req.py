import requests as rq

v_url = "https://10.36.0.73:5055/check?name=test&patronym=testovich&lastname=testov&username=tcell_2ad5kn21e88w36ag"
r = rq.get(v_url , verify=False)
print('Content-Type: text/plain')
print("")

print(r.text)

