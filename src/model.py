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
    benefit_value: float
    benefit_pct: int

    def __init__(self, action_data):
        name, cost, benefit_pct = action_data
        self.name = name
        self.cost = cost
        self.benefit_pct = benefit_pct
        self.benefit_value = self.get_action_benefit_value()

    def get_action_benefit_value(self):
        return (self.cost * self.benefit_pct) / 100


@dataclass
class Portfolio:
    """Class for portfolios"""
    data: List[Action]
    repartition: List[int]
    cost: int
    benefit_value: float
    benefit_pct: float

    def __init__(self, data, repartition=False):
        self.data = data
        self.repartition = self.get_portfolio_repartition(repartition)
        self.cost = self.get_portfolio_cost()
        self.benefit_value = self.get_portfolio_benefit_value()
        self.benefit_pct = self.get_portfolio_benefit_pct()

    def get_portfolio_repartition(self, repartition):
        if repartition:
            return repartition
        else:
            return [1 for _ in self.data]

    def get_portfolio_cost(self):
        """Method to get portfolio total cost"""
        return sum([action.cost for action in self.data if self.repartition[self.data.index(action)] == 1])

    def get_portfolio_benefit_value(self):
        """Method to get portfolio total benefit in value"""
        result = 0
        for action in [action for action in self.data if self.repartition[self.data.index(action)] == 1]:
            result += action.cost * action.benefit_pct / 100
        return result

    def get_portfolio_benefit_pct(self):
        """Method to get portfolio total benefit in percentage"""
        if self.cost == 0:
            return 0
        else:
            return ((self.cost + self.benefit_value) / self.cost - 1) * 100

