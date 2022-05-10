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
    cost: int
    performance: int

    @property
    def benefit_value(self):
        return (self.cost * self.performance) / 100

    @property
    def value_after_two_years(self):
        """Method to get the total value of the action after two years"""
        return self.cost + self.benefit_value


@dataclass
class Portfolio:
    """Class for portfolios"""
    data: List[Action]

    @property
    def cost(self):
        """Method to get portfolio total cost"""
        return sum([action.cost for action in self.data])

    @property
    def benefit_value(self):
        """Method to get portfolio total benefit in value"""
        return sum([action.benefit_value for action in self.data])

    @property
    def performance(self):
        """Method to get portfolio total benefit in percentage"""
        return (self.benefit_value / self.cost) * 100 if self.cost > 0 else 0

    @property
    def value_after_two_years(self):
        """Method to get the total value of the portfolio after two years"""
        return self.cost + self.benefit_value
