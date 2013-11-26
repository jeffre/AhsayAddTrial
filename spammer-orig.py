import httplib, urllib, sys
from pprint import pprint

#convert 2 digit hex into 8 digits then decode to ASCII 
def getChar(hex):
  return '000000'.decode('hex')+hex.decode('hex')

#create a 2 digit hex of a vars length
def getHexLength(var):
  if len("%x" % len(var)) < 2:
    return '0'+"%x" % len(var)
  else:
    return "%x" % len(var)

#clean the code
params = ''
def add(var1, var2):
  global params
  #every pair of variable and value is encased by P; they are individually precusored
  #by an 8 digit hex that must equal the length of its respective variable or value
  params += 'P'+getChar(getHexLength(var1))+var1+getChar(getHexLength(var2))+var2+'P'

def ahsaypad(key, val):
	global params
	o_key	= str(len(key)).zfill(8).decode('hex')+key
	o_val 	= str(len(val)).zfill(8).decode('hex')+val
	o	= o_key + o_val
	params += 'P'+o+'P'
	
#the cycle
accountscreated = 0 
accountsfailed = 0 
def run(var):
  global params
  global accountscreated
  global accountsfailed
  for i in range(1,var+1):
    username = 'username_' + str(i)
    alias = 'alias' + str(i)
    password = 'password'
    email = 'user'  + str(i) + '@email.com'
    language = 'en'
    timezone = 'GMT-07:00 (MST)'
    seq = '1'
    e = 'N'
    b = 'N'

    add('LOGIN_NAME', username)	#required
    pprint(params)
    sys.exit()
    add('B', b)
    add('PASSWORD', password)	#required
    add('TIMEZONE', timezone)
    add('SEQ', seq)
    add('ALIAS', alias)
    add('EMAIL', email)
    add('LANGUAGE', language)
    add('E', e)
    #add('ReferralKey', ReferralKey)

    print params
    conn = httplib.HTTPConnection("eval.ahsay.com")
    #conn.request("POST", "/obs/obm5.5/NewTrial.obc", params)	#registers OBM agent
    conn.request("POST", "/obs/acb5.5/NewTrial.obc", params)	#registers ACB agent
    response = conn.getresponse()
    #print response.status, response.reason, response.getheader('server')
    data = response.read()
    if "OK" in data:
      accountscreated = accountscreated + 1
      print username + " (" + alias + ") created"
    else:
      accountsfailed = accountsfailed + 1
      if "NO_TRIAL_HOME" in data:
        #print 'Server is full.  No more trials can be created.'
        print data
        return
      else:
        print 'Error Response: "' + data[data.find("<Reply><")+8:data.find("/></Reply>")] + '" ' + username + " (" + alias + ")"
    conn.close()
    params = ''
    
#Max number of trials to create
run(7)
print "Finished:", accountscreated, " created,", accountsfailed, "skipped."
