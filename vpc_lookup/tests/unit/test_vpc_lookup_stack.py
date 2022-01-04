import aws_cdk as core
import aws_cdk.assertions as assertions

from vpc_lookup.vpc_lookup_stack import VpcLookupStack

# example tests. To run these tests, uncomment this file along with the example
# resource in vpc_lookup/vpc_lookup_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = VpcLookupStack(app, "vpc-lookup")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
