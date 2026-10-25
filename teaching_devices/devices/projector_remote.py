from teaching_devices.core import DeviceStatus
from ._validation import require_percent
from .teaching_device import TeachingDevice


class ProjectorRemote(TeachingDevice):
    def __init__(self, device_id: str, name: str, location: str, battery_level: int):
        super().__init__(device_id, name, location)
        self._battery_level = require_percent(battery_level, "battery_level")

    @property
    def battery_level(self) -> int:
        return self._battery_level

    def is_ready_for_use(self) -> bool:
        return self.status == DeviceStatus.AVAILABLE and self._battery_level >= 20

    def get_default_priority_score(self) -> float:
        return float(self._battery_level)

    def __repr__(self) -> str:
        return super().__repr__() + f", pin={self._battery_level}%"
