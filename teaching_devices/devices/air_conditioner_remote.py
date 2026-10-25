from typing import Iterable

from teaching_devices.core import DeviceStatus
from .teaching_device import TeachingDevice


class AirConditionerRemote(TeachingDevice):
    def __init__(self, device_id: str, name: str, location: str, compatible_rooms: Iterable[str]):
        super().__init__(device_id, name, location)
        self._compatible_rooms = frozenset(r.strip().upper() for r in compatible_rooms)

    @property
    def compatible_rooms(self) -> frozenset[str]:  
        return self._compatible_rooms

    def is_compatible_with(self, room_id: str) -> bool:
        return room_id.strip().upper() in self._compatible_rooms

    def is_ready_for_use(self) -> bool:
        return self.status == DeviceStatus.AVAILABLE

    def get_default_priority_score(self) -> float:
        return 100.0 if self._compatible_rooms else 0.0

    def __repr__(self) -> str:
        return super().__repr__() + f", phòng={'/'.join(sorted(self._compatible_rooms))}"
