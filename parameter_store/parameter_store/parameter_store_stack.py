from aws_cdk import (
    # Duration,
    Stack,
    aws_ssm as ssm,
    CfnOutput,
    # aws_sqs as sqs,
)
from constructs import Construct

class ParameterStoreStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        string_param = ssm.StringParameter.value_for_string_parameter(self, "string-parameter")

        string_param_lookup = ssm.StringParameter.value_from_lookup(self, "string-parameter")

        CfnOutput(self, "deployment-parameter", value=string_param)

        CfnOutput(self, 'synthesis-parameter', value=string_param_lookup)