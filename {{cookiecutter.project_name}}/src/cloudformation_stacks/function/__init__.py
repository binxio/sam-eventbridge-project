from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser, envelopes

from .event import CloudFormationEvent


logger = Logger()


@event_parser(model=CloudFormationEvent, envelope=envelopes.EventBridgeEnvelope)
def handler(event: CloudFormationEvent, context: LambdaContext) -> None:
    logger.info(f"Stack: {event.stack_id} is in {event.status_details.status}")

    if event.status_details.status_reason:
        logger.info(f"Reason: {event.status_details.status_reason}")
