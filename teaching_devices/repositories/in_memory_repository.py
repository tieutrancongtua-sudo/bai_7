from typing import Callable, Optional

from teaching_devices.exceptions import DuplicateIdException
from .i_repository import IRepository, TId


class InMemoryRepository(IRepository[TId]):
    def __init__(self) -> None:
        self._items: dict[str, TId] = {}

    def add(self, item: TId) -> None:
        if item is None:
            raise ValueError
        if item.id in self._items:
            raise DuplicateIdException(item.id)
        self._items[item.id] = item

    def remove(self, item_id: str) -> bool:
        return self._items.pop(item_id, None) is not None

    def find_by_id(self, item_id: str) -> Optional[TId]:
        return self._items.get(item_id)

    def get_all(self) -> tuple[TId, ...]:
        return tuple(self._items.values()) 

    def find_all(self, condition: Callable[[TId], bool]) -> tuple[TId, ...]:
        if condition is None:
            raise ValueError
        return tuple(x for x in self._items.values() if condition(x))
