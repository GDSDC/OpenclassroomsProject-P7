# IMPORTS
from dataclasses import dataclass
from typing import List

# RULES
ACTION_PURCHASE_LIMIT = 1
ACTION_MINIMUM_FRACTION = 1
MAXIMUM_PURCHASE_COST: int = 500


# CLASSES
@dataclass
class Action:
    """Class for actions"""
    name: str
    cost: float
    performance: float

    @property
    def benefit_value(self) -> float:
        return (self.cost * self.performance) / 100

    @property
    def value_after_two_years(self) -> float:
        """Method to get the total value of the action after two years"""
        return self.cost + self.benefit_value

    @property
    def efficiency(self) -> float:
        """Method to get efficeny of an action"""
        return self.performance / self.cost


@dataclass
class Portfolio:
    """Class for portfolios"""
    actions: List[Action]

    @property
    def cost(self) -> float:
        """Method to get portfolio total cost"""
        return sum([action.cost for action in self.actions]) if self.actions else 0

    @property
    def benefit_value(self) -> float:
        """Method to get portfolio total benefit in value"""
        return sum([action.benefit_value for action in self.actions]) if self.actions else 0

    @property
    def performance(self) -> float:
        """Method to get portfolio total benefit in percentage"""
        return (self.benefit_value / self.cost) * 100 if self.cost > 0 else 0

    @property
    def value_after_two_years(self) -> float:
        """Method to get the total value of the portfolio after two years"""
        return self.cost + self.benefit_value
