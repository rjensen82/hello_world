import subprocess
import json

#Deploy API
#NOTE: When deploying an API the first time, you can combine the stage creation and deployment creation at the same time:
#Hardcoded values due to time constraints
api_id='5er9ozc9sc'
region='us-west-2'
stage_name='dev'
#define AWS CLI command that will be executed. These values could get user input from user args like curl_test.py
create_deployment = "aws apigateway create-deployment --rest-api-id "+api_id+" --region "+region+" --stage-name "+stage_name
create_deployment_dump = subprocess.Popen([create_deployment], shell=True, stdout=subprocess.PIPE)
create_deployment_out = create_deployment_dump.stdout.read()
create_deployment_obj = json.loads(create_deployment_out)
print create_deployment_obj

#Code for python2.7 Lambda function created below using AWS CLI
python_lambda_code= '''
from __future__ import print_function
import json
print('Loading function')

def lambda_handler(event, context):
    return "Hello "+event['name']+" World!"  # Echo back the event value
'''
#description - hardcoded for now.
description="Setting up a lambda using python2.7 and some code"

#AWS CLI command to create Lambda with inserted code, description, etc
create_lambda = '''\
create-function \
--function-name get_function \
--runtime "python2.7" \
--role %s \
--handler lambda_function.lambda_handler \
--code %s \
--description %s \
--timeout 10 \
--memory-size 128
''' % ("{user_supplied_iam_role_for_creating_lambda}", python_lambda_code, description)

#execute the lambda creation and print output
create_lambda_dump = subprocess.Popen([create_lambda], shell=True, stdout=subprocess.PIPE)
create_lambda_out = create_lambda_dump.stdout.read()
create_lambda_obj = json.loads(create_lambda_out)
print create_lambda_obj
# aws apigateway create-deployment --region <region> \
#    --rest-api-id <rest-api-id> \
#    --stage-name <stage-name>