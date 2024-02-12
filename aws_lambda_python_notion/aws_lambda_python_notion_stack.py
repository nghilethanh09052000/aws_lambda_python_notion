from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda
)
from constructs import Construct

class AwsLambdaPythonNotionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        f1_search_page_or_database = aws_lambda.Function(
            self,
            id='f1_search_page_or_database',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_notion/functions'),
            handler='f1_search_page_or_database.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )

        f2_create_page = aws_lambda.Function(
            self,
            id='f2_create_page',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_notion/functions'),
            handler='f2_create_page.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )

        f3_add_row = aws_lambda.Function(
            self,
            id='f3_add_row',
            code=aws_lambda.Code.from_asset('./aws_lambda_python_notion/functions'),
            handler='f3_add_row.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )