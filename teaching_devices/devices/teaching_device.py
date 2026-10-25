from abc import ABC, abstractmethod

from teaching_devices.core import DeviceStatus
from teaching_devices.exceptions import DeviceNotReadyException
from ._validation import require_text


class TeachingDevice(ABC):
    def __init__(self, device_id: str, name: str, storage_location: str):
        self._id = require_text(device_id, "id")
        self._name = require_text(name, "name")
        self._storage_location = require_text(storage_location, "storage_location")
        self._status = DeviceStatus.AVAILABLE

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def storage_location(self) -> str:
        return self._storage_location

    @property
    def status(self) -> DeviceStatus:
        return self._status

    @abstractmethod
    def is_ready_for_use(self) -> bool: ...

    @abstractmethod
    def get_default_priority_score(self) -> float: ...

    def borrow(self) -> None:
        if not self.is_ready_for_use():
            raise DeviceNotReadyException(self.id, self._status)
        self._status = DeviceStatus.BORROWED

    def return_device(self) -> None: 
        if self._status != DeviceStatus.BORROWED:
            raise RuntimeError(f"Thiết bị '{self.id}' không ở trạng thái Borrowed.")
        self._status = DeviceStatus.AVAILABLE

    def send_to_maintenance(self) -> None:
        if self._status == DeviceStatus.BORROWED:
            raise RuntimeError("Không thể bảo trì thiết bị đang được mượn.")
        self._status = DeviceStatus.UNDER_MAINTENANCE

    def __repr__(self) -> str:
        return f"{type(self).__name__}[{self.id}] {self.name} - {self._status.value}"
