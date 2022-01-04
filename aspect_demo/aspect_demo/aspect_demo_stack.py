from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    aws_lambda as lambda_,
    IAspect,
    Aspects,
    aws_s3_notifications,
    Annotations,
    Tags,
    # aws_sqs as sqs,
)
from constructs import Construct
import jsii

class AspectDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        role = iam.Role(
            self, 'lambda_role',
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="lambda_role"
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )

        # Create s3 bucket
        source_bucket = s3.Bucket(
            self, "cdk-source-bucket",
            bucket_name="demo-source-865"
        )
        dest_bucket = s3.Bucket(
            self, "cdk-dest-bucket",
            bucket_name="demo-dest-865",
            encryption=s3.BucketEncryption.KMS_MANAGED
        )

        # Create Lambda function
        function = lambda_.Function(
            self, "lambda_function",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            environment={
                'DestinationBucket': dest_bucket.bucket_name
            },
            role=role, 
            code=lambda_.Code.from_asset("./lambda")
        )

        # Create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # Assign notification for the s3 event type (ex: OBJECT_CREATED)
        source_bucket.add_object_created_notification(notification)        

        Aspects.of(self).add(EncryptionAspect())
        Tags.of(self).add("key", "value")
        Tags.of(self).add("Project", "demo-app")

@jsii.implements(IAspect)
class EncryptionAspect:
    def visit(self, construct):
        if isinstance(construct, s3.CfnBucket):
            if str(construct.bucket_name) == "demo-dest-865":
                if str(construct.bucket_encryption) == 'None':
                    Annotations.of(construct).add_error("Destination Bucket should be encrypted!!!")
