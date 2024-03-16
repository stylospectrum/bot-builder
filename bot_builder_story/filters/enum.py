import enum


class FilterOperator(str, enum.Enum):
    And = "And"
    Or = "Or"
    Equal = "Equal"
