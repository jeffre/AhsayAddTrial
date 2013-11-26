import httplib, urllib

url 	= 'eval.ahsay.com'
accounts	= [{
		'LOGIN_NAME'	: 'username4',
		'PASSWORD'	: 'password',
		'EMAIL'		: 'ahsay@mailinator.com'
	},{
		'LOGIN_NAME'	: 'username5',
		'PASSWORD'	: 'password',
		'EMAIL'		: 'ahsay@mailinator.com'
}]
shared	={
	'TIMEZONE'		: 'GMT-07:00 (MST)',
	'agent'		: 'obm',
	'LANGUAGE'	: 'en',
	'SEQ'		: '1',
	'E'			: 'N',
	'B'			: 'N'
}
agent = 'acb'

def main():
	for a in accounts:
		post_data = ""
		for key, val in a.iteritems():
			post_data += ahsaypad(key, val)
			
		for key, val in shared.iteritems():
			post_data += ahsaypad(key, val)

		conn = httplib.HTTPConnection(url)
		conn.request("POST", "/obs/"+agent+"5.5/NewTrial.obc", post_data)	#registers ACB agent
		response = conn.getresponse()
		http_response = response.read()
		print http_response

def ahsaypad(key, val):
	n	= '000000'.decode('hex')
	o	= n + chr(len(key)) + key
	o	+= n+ chr(len(val)) + val
	return 'P'+o+'P'
    
if __name__ == "__main__":
	main()
