from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar

T = TypeVar("T")


class ISelectionStrategy(ABC, Generic[T]):
    @abstractmethod
    def select(self, candidates: Sequence[T]) -> T: ...
