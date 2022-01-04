import aws_cdk as core
import aws_cdk.assertions as assertions

from secret_manager.secret_manager_stack import SecretManagerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in secret_manager/secret_manager_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SecretManagerStack(app, "secret-manager")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
