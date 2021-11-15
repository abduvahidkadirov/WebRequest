import cgi

v_url = "https://10.36.0.73:5055/"
v_username = "tcell_2ad5kn21e88w36ag"
vErrCode = 0
vErrMsg = "Successfull"        

#rp=cgi.FieldStorage()
#RespList = list(rp)
#vAction  = rp.getvalue("action")
#if "name" in RespList: vName =  rp.getvalue("name")
#if "surname" in RespList: vSurName =  rp.getvalue("surname")
#if "middlename" in RespList: vMiddleName =  rp.getvalue("middlename")

#v_url = "https://10.36.0.73:5055/check?name=test&patronym=testovich&lastname=testov&username=tcell_2ad5kn21e88w36ag"

def PrintMsg():
        print("{ ""ErrCode"": "" " + str(vErrCode) + " "", ""ErrMsg"":  "" " + vErrMsg + " ""} " )
        exit()
        pass