from abc import ABC, abstractmethod
from typing import Callable, Generic, Optional, Sequence, TypeVar

from teaching_devices.core import IIdentifiable

TId = TypeVar("TId", bound=IIdentifiable)


class IRepository(ABC, Generic[TId]):
    @abstractmethod
    def add(self, item: TId) -> None: ...

    @abstractmethod
    def remove(self, item_id: str) -> bool: ...

    @abstractmethod
    def find_by_id(self, item_id: str) -> Optional[TId]: ...

    @abstractmethod
    def get_all(self) -> Sequence[TId]: ...

    @abstractmethod
    def find_all(self, condition: Callable[[TId], bool]) -> Sequence[TId]: ...
