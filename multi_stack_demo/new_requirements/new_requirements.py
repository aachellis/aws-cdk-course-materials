from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
)

from constructs import Construct 

class NewRequirements(Stack):

    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Craete dynamodb table
        dynamo_table = dynamodb.Table (
            self, 'demo-table',
            partition_key=dynamodb.Attribute(
                name='id',
                type=dynamodb.AttributeType.STRING
            )
        )

        # create lambda function
        second_function = lambda_.Function(
            self, "second_lambda_function",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            function_name="second_lambda",
            environment={
                'TABLE_NAME': dynamo_table.table_name,
            },
            code=lambda_.Code.from_asset("./lambda/write_to_dynamo")
        )

        self._lambda_function = second_function

    @property
    def second_function(self):
        return self._lambda_function