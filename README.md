# hello_world
Welcome to the README.md for my basic 'greetings microservice'. The microservice was created with Lambda and API Gateway.

This repo assumes you have an AWS account with proper access/permissions to AWS.


-----Q and A-----:

Is the service resonably resiliant? 
YES, it is backed by Lambda to prevent single node failures

Can the service be scaled, preferably automatically, to handle increased loads?
YES, you can scale using API Gateway in various ways. Such as enabling Cache capacity and increasing burst and ate thresholds. The baseline rate is 10000 requests per second without any tweaking!

-----Testing------:

The test script is run with:
python curl_test.py <env>

A name can also be specified if you desire:
python curl_test.py <env> <name_for_post>
