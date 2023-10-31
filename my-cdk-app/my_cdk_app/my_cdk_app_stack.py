from aws_cdk import (
    # Duration,
    Stack,
    
    # aws_sqs as sqs,
)
from aws_cdk import core
from aws_cdk import aws_lambda
from constructs import Construct

class MyCdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # The code that defines your stack goes here
        hello_fucntion = aws_lambda.Function(self, id ="HelloFunctionv2", code = aws_lambda.Code.from_asset("./compute"),runtime=aws_lambda.Runtime.PYTHON_3_8)
        # example resource
        # queue = sqs.Queue(
        #     self, "MyCdkAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
