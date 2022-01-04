from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
    # aws_sqs as sqs,
)
from constructs import Construct

class VpcLookupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id='vpc-0486bb014529f422b')

        subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        CfnOutput(
            self, "publicSubnets",
            value=str(subnets.subnet_ids)
        )
