from typing import Callable, Generic, Optional, TypeVar

from teaching_devices.devices import TeachingDevice
from teaching_devices.repositories import IRepository
from teaching_devices.strategies import ISelectionStrategy

D = TypeVar("D", bound=TeachingDevice)


class AllocationService(Generic[D]):
    def __init__(self, repository: IRepository[D], strategy: ISelectionStrategy[D]):
        if repository is None or strategy is None:
            raise ValueError
        self._repository = repository
        self._strategy = strategy

    def change_strategy(self, new_strategy: ISelectionStrategy[D]) -> None:
        if new_strategy is None:
            raise ValueError
        self._strategy = new_strategy

    def allocate(self, additional_condition: Optional[Callable[[D], bool]] = None) -> D:
        candidates = self._repository.find_all(
            lambda d: d.is_ready_for_use() and (additional_condition is None or additional_condition(d)))
        selected = self._strategy.select(candidates)  
        selected.borrow()
        return selected
