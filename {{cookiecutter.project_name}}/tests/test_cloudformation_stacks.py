from typing import List
import json
import pytest
import os
import glob

from src.cloudformation_stacks.function import handler  # type: ignore
from aws_lambda_powertools.utilities.typing import LambdaContext


def get_payloads(type: str) -> List[dict]:
    events = []
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "payloads"))
    payloads = glob.glob(f"{path}/{type}_*.json")

    for payload in payloads:
        with open(payload) as fh:
            events.append(json.load(fh))

    return events


@pytest.mark.parametrize("event", get_payloads(type="cloudformation"))
def test_invoke_payloads(event: dict) -> None:
    assert handler(event, LambdaContext()) == None
