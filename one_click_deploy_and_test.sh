#!/bin/bash

/usr/bin/python deploy_api_gateway_and_lambda.py
/usr/bin/python curl_test.py dev
