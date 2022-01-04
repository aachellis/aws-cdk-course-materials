#!/usr/bin/env python3
import os

import aws_cdk as cdk

from vpc_lookup.vpc_lookup_stack import VpcLookupStack


app = cdk.App()
VpcLookupStack(app, "VpcLookupStack",
    env={
        'account': os.environ["CDK_DEFAULT_ACCOUNT"],
        'region': os.environ["CDK_DEFAULT_REGION"]
    }
)

app.synth()
