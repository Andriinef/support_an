from enum import Enum
from functools import lru_cache

__all__ = ["Role"]


class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

    @classmethod
    @lru_cache
    def values(cls) -> list[tuple[str, str]]:
        result = [(element.value, element.value.capitalize()) for element in cls]
        return result
