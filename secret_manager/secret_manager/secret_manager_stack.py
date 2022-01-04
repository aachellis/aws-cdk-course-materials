from aws_cdk import (
    # Duration,
    Stack,
    aws_secretsmanager as sm,
    aws_iam as iam,
    aws_kms as kms,
    # aws_sqs as sqs,
)
from constructs import Construct

class SecretManagerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        key = kms.Key.from_key_arn(self, "kms-key", "arn:aws:kms:ap-south-1:386768119616:key/ffd92422-cb1e-424d-b87d-85d580c29baf")

        secret = sm.Secret.from_secret_attributes(
            self, "secret",
            secret_arn="arn:aws:secretsmanager:ap-south-1:386768119616:secret:user_password-w6a6Tb",
            encryption_key=key
        )

        iam.User(self, "user", password=secret.secret_value)
