# hello_world
Welcome to the README.md for my basic 'greetings microservice'. The microservice was created with Lambda and API Gateway.

This repo assumes you have an AWS account with proper access/permissions to AWS in order to build the stack using Terraform.


# Sample URL for testing GET and POST
https://5er9ozc9sc.execute-api.us-west-2.amazonaws.com/prod/helloworld

NOTE: can change prod to any of dev, test, demo and prod




# Questions and Answers About Project

Is the service resonably resiliant?

YES, it is backed by Lambda to prevent single node failures

Can the service be scaled, preferably automatically, to handle increased loads?

YES, you can scale using API Gateway in various ways. Such as enabling Cache capacity and increasing burst and ate thresholds. The baseline rate is 10000 requests per second without any tweaking!



# Testing Using curl_test.py

The test script is run with:

python curl_test.py <env>

A name can also be specified if you desire:

python curl_test.py <env> <name_for_post>
