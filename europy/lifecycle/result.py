from enum import Enum
from typing import Union, List

from _pytest.mark import Mark
from pandas import DataFrame


class TestLabel(str, Enum):
    BIAS = "bias"
    DATA_BIAS = "data-bias"
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    UNIT = "unit"
    INTEGRATION = "integration"
    ACCURACY = "accuracy"
    MINIMUM_FUNCTIONALITY = "minimum-functionality"

    @staticmethod
    def of(mark: Mark):
        return TestLabel(mark.name)

    def __json__(self):
        return str(self.value)


class TestResult:
    def __init__(self, key: str,
                 labels: List[Union[str, TestLabel]],
                 result: Union[float, str, bool, DataFrame],
                 description: str):
        self.key = key
        self.description = description
        self.labels = labels
        self.result = result