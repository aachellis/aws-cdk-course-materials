import aws_cdk as core
import aws_cdk.assertions as assertions

from aspect_demo.aspect_demo_stack import AspectDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aspect_demo/aspect_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AspectDemoStack(app, "aspect-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
