from abc import ABC, abstractmethod
from typing import Any


class BaseDB(ABC):
    @abstractmethod
    async def get_all(self, session: Any) -> list[Any]: ...

    @abstractmethod
    async def add(self, obj: Any, session: Any) -> None: ...
