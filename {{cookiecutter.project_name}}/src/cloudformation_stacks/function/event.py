from typing import Optional
from aws_lambda_powertools.utilities.parser import BaseModel, Field


class CloudFormationStatusDetails(BaseModel):
    status: str
    status_reason: str = Field(alias="status-reason")


class CloudFormationEvent(BaseModel):
    stack_id: str = Field(alias="stack-id")
    status_details: CloudFormationStatusDetails = Field(alias="status-details")
