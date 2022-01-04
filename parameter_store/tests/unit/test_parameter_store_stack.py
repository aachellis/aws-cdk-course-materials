import aws_cdk as core
import aws_cdk.assertions as assertions

from parameter_store.parameter_store_stack import ParameterStoreStack

# example tests. To run these tests, uncomment this file along with the example
# resource in parameter_store/parameter_store_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ParameterStoreStack(app, "parameter-store")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
