import aws_cdk as core
import aws_cdk.assertions as assertions

from multi_stack_demo.multi_stack_demo_stack import MultiStackDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in multi_stack_demo/multi_stack_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MultiStackDemoStack(app, "multi-stack-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
