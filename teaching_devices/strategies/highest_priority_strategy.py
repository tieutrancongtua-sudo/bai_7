from typing import Callable, Sequence

from teaching_devices.exceptions import NoSuitableItemException
from .i_selection_strategy import ISelectionStrategy, T


class HighestPriorityStrategy(ISelectionStrategy[T]):
    def __init__(self, score_selector: Callable[[T], float]):
        if score_selector is None:
            raise ValueError
        self._score_selector = score_selector

    def select(self, candidates: Sequence[T]) -> T:
        if not candidates:
            raise NoSuitableItemException()
        return max(candidates, key=self._score_selector)
