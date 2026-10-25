from typing import Protocol


class IIdentifiable(Protocol):

    @property
    def id(self) -> str: ...
