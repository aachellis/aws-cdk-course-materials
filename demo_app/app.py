#!/usr/bin/env python3
import os

import aws_cdk as cdk

from demo_app.demo_app_stack import DemoAppStack

default = cdk.Environment(account='386768119616', region='ap-south-1')
prod = cdk.Environment(account='725124995909', region='ap-south-1')


app = cdk.App()
DemoAppStack(app, "DemoAppStack",
    env=default, prod_env=False
)

DemoAppStack(app, "DemoAppStackProd",
    env=prod, prod_env=True
)

app.synth()
