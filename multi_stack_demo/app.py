#!/usr/bin/env python3
import os

import aws_cdk as cdk

from multi_stack_demo.multi_stack_demo_stack import MultiStackDemoStack
from demo_app.demo_app import DemoApp
from new_requirements.new_requirements import NewRequirements

env = cdk.Environment(
    account=os.environ['CDK_DEFAULT_ACCOUNT'],
    region=os.environ['CDK_DEFAULT_REGION']
)


app = cdk.App()

new_req = NewRequirements(app, "new-requirements", env=env)
DemoApp(app, "demo-app", env=env, new_lambda=new_req.second_function)
# MultiStackDemoStack(app, "MultiStackDemoStack",)

app.synth()
