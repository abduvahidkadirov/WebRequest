import requests as rq
import cgi
import ini


print('Content-Type: text/plain')
#print('Content-Type: application/json')
print("")

rp=cgi.FieldStorage()
RespList = list(rp)

if "action" not in RespList: 
	ini.vErrCode = -101
	ini.vErrMsg = "NoFoundParam ACTION"
	ini.PrintMsg()

vAction  = rp.getvalue("action")

#Если это запрос на проверку в ЧС
if vAction == "check":
	v_url = ini.v_url + "check?username="  + ini.v_username 

	if "name" in RespList :
		v_url = v_url + "&name=" + rp.getvalue("name")
	else:
		ini.vErrCode = -101
		ini.vErrMsg = "NoFoundParam NAME"
		ini.PrintMsg()
		
	if "surname" in RespList :
		v_url = v_url + "&lastname=" + rp.getvalue("surname")
	else: 
		ini.vErrCode = -101
		ini.vErrMsg = "NoFoundParam SURNAME"
		ini.PrintMsg()

	if "middlename" in RespList :
		v_url = v_url + "&patronym=" + rp.getvalue("middlename")
#	else: sys.exit() #print("NoFoundParam MIDDLE NAME")
elif vAction == "req":
	ini.vErrMsg = "Credit Query"
	ini.PrintMsg()

else:
	ini.vErrCode = -100
	ini.vErrMsg = "Invalid action comands"
	ini.PrintMsg()

#print(v_url)
	
r = rq.get(v_url , verify=False)
JsonString = r.json()

DictKey = list(JsonString)

if 'Answer' in DictKey:
#	print("Answer:" + json_string["Answer"])
	ini.vErrMsg = JsonString["Answer"]
else:
	ini.ErrCode = -2
	ini.vErrMsg = JsonString
	
ini.PrintMsg()