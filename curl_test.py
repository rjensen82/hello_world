import requests
import sys

#Define various portions of uri to make generic. In this case only stage name becomes generic
def run_test(environment, name):
	restapi_id="5er9ozc9sc"
	region="us-west-2"
	stage_name=environment+"/helloworld"
	url = "https://%s.execute-api.%s.amazonaws.com/%s"%(restapi_id, region, stage_name)
	print "Running against url:", url


	#use requests to GET
	print "\n---------------\n   GET TEST\n---------------"
	r = requests.get(url)
	get_status_code = r.status_code
	print "Status code of GET: %s" % (get_status_code)
	get_request_body = r.content
	print "GET body content returned: %s" % (get_request_body)
	if get_request_body == '"Hello World!"':
		print "*GET test passed*"
	else:
		sys.exit("GET test FAILED!")

	#use requests to POST the name in JSON
	print "\n---------------\n   POST TEST\n---------------"
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	s = requests.post(url, json={"name": name})
	post_status_code = s.status_code
	print "Status code of POST: %s" % (post_status_code)
	post_request_body = s.content
	print "POST body content returned: %s" % (post_request_body)
	post_expected_output='"Hello %s World!"'%(name)
	if post_request_body == post_expected_output:
		print "POST test passed"
	else:
		sys.exit("POST test FAILED!")

	#Only makes it this far if both GET and POST passed tests above
	print "\n---------------\n   SUMMARY\n---------------"
	print "Both GET and POST have passed for env: %s" % (environment)

if __name__ == "__main__":
	#Get the environment and name - or autofill name
	if len(sys.argv)<2:
		sys.exit("Usage:\nNOTE:<name_for_post> is optional\npython curl_test.py <env> <name_for_post>\n")
	environment = sys.argv[1]
	#check to make sure env is valid before moving on
	allowed_envs=["dev", "test", "demo", "prod"]
	if environment not in allowed_envs:
		sys.exit("Invalid environment! Select from dev, test, demo or prod")
	#generate a fakeout name if not specified by user
	if len(sys.argv)==2:
		name="Fakeout Name"
	elif len(sys.argv)==3:
		name = sys.argv[2]
	else:
		sys.exit("Usage:\nNOTE:<name_for_post> is optional\npython curl_test.py <env> <name_for_post>\n")

	#print something so user knows test is initiating and then run test against env
	print "---------------\nBEGIN CURL TEST\n---------------\n"
	run_test(environment, name)





