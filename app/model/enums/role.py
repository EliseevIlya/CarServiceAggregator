import enum


class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    ORGANIZATION = "organization"
