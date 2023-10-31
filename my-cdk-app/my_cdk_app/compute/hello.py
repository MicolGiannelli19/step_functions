import json

def hello():
    # print("check 1")
    return "Hello Jodeci and Micol"

def lambda_handler(event, context): 
    message = hello()
    return {
        'statusCode':200,
        'body': json.dumps({"meassage": message})
    }