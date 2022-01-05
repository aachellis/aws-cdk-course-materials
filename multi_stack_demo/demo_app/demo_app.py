from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3_notifications,
    # aws_sqs as sqs,
)
from constructs import Construct

class DemoApp(Stack):

    def __init__(self, scope: Construct, construct_id: str, new_lambda, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Lambda Role
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
        if prod_env:
            source_bucket = s3.Bucket(
                self, "cdk-source-bucket",
                bucket_name="demo-source-865-prod"
            )
            dest_bucket = s3.Bucket(
                self, "cdk-dest-bucket",
                bucket_name="demo-dest-865-prod"
            )
        else:
            source_bucket = s3.Bucket(
                self, "cdk-source-bucket",
                bucket_name="demo-source-865-nonprod"
            )
            dest_bucket = s3.Bucket(
                self, "cdk-dest-bucket",
                bucket_name="demo-dest-865-nonprod"
            )

        # Create Lambda function
        first_function = lambda_.Function(
            self, "first_lambda_function",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            environment={
                'DestinationBucket': dest_bucket.bucket_name
            },
            role=role, 
            code=lambda_.Code.from_asset("./lambda/copy-object")
        )

        # Create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(first_function)

        # Assign notification for the s3 event type (ex: OBJECT_CREATED)
        source_bucket.add_object_created_notification(notification)

        new_notification = aws_s3_notifications.LambdaDestination(new_lambda)
        dest_bucket.add_object_created_notification(new_notification)
