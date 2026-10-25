from typing import Sequence

from teaching_devices.exceptions import NoSuitableItemException
from .i_selection_strategy import ISelectionStrategy, T


class FirstAvailableStrategy(ISelectionStrategy[T]):
    def select(self, candidates: Sequence[T]) -> T:
        if not candidates:
            raise NoSuitableItemException()
        return candidates[0]
