from teaching_devices.core import DeviceStatus


class DeviceNotReadyException(Exception):
    def __init__(self, device_id: str, current_status: DeviceStatus):
        super().__init__(f"Thiết bị '{device_id}' chưa sẵn sàng (trạng thái: {current_status.value}).")
        self.device_id = device_id
        self.current_status = current_status
