from teaching_devices.core import DeviceStatus
from ._validation import require_percent
from .teaching_device import TeachingDevice


class WirelessMicrophone(TeachingDevice):
    def __init__(self, device_id: str, name: str, location: str, battery_level: int, signal_quality: int):
        super().__init__(device_id, name, location)
        self._battery_level = require_percent(battery_level, "battery_level")
        self._signal_quality = require_percent(signal_quality, "signal_quality")

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @property
    def signal_quality(self) -> int:
        return self._signal_quality

    def is_ready_for_use(self) -> bool:
        return (self.status == DeviceStatus.AVAILABLE
                and self._battery_level >= 30 and self._signal_quality >= 40)

    def get_default_priority_score(self) -> float:
        return (self._battery_level + self._signal_quality) / 2

    def __repr__(self) -> str:
        return super().__repr__() + f", pin={self._battery_level}%, tín hiệu={self._signal_quality}%"
