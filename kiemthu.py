"""Kiểm thử Lab W07. Chạy: python main.py (Python 3.10+)."""
from teaching_devices.devices import AirConditionerRemote, ProjectorRemote, WirelessMicrophone
from teaching_devices.exceptions import DuplicateIdException, NoSuitableItemException
from teaching_devices.repositories import InMemoryRepository
from teaching_devices.services import AllocationService
from teaching_devices.strategies import FirstAvailableStrategy, HighestPriorityStrategy


def header(text: str) -> None:
    print(f"\n=== {text} ===")


def main() -> None:
    projectors: InMemoryRepository[ProjectorRemote] = InMemoryRepository()
    acs: InMemoryRepository[AirConditionerRemote] = InMemoryRepository()
    mics: InMemoryRepository[WirelessMicrophone] = InMemoryRepository()

    header("1. Thêm thiết bị")
    projectors.add(ProjectorRemote("PJ01", "Remote Epson", "Kho A", 80))
    projectors.add(ProjectorRemote("PJ02", "Remote Sony", "Kho A", 15))
    projectors.add(ProjectorRemote("PJ03", "Remote BenQ", "Kho B", 55))
    acs.add(AirConditionerRemote("AC01", "Remote Daikin", "Kho A", ["A101", "A203"]))
    acs.add(AirConditionerRemote("AC02", "Remote LG", "Kho B", ["B101"]))
    mics.add(WirelessMicrophone("MIC01", "Micro Shure", "Kho A", 90, 30))
    mics.add(WirelessMicrophone("MIC02", "Micro Sony", "Kho A", 60, 70))
    mics.add(WirelessMicrophone("MIC03", "Micro AKG", "Kho B", 85, 90))
    print(f"Máy chiếu: {len(projectors.get_all())}, Điều hòa: {len(acs.get_all())}, Micro: {len(mics.get_all())}")

    header("2. Thêm trùng mã")
    try:
        projectors.add(ProjectorRemote("PJ01", "Trùng", "Kho C", 50))
    except DuplicateIdException as ex:
        print(f"Bắt được DuplicateIdException: {ex.duplicate_id}")

    header("3. Tìm theo mã")
    print(projectors.find_by_id("PJ03"))
    print("XXX -> None" if projectors.find_by_id("XXX") is None else "lỗi")

    header("4. Lọc thiết bị sẵn sàng")
    for d in mics.find_all(lambda m: m.is_ready_for_use()):
        print(d)

    header("5. Máy chiếu: HighestPriority")
    pj_service = AllocationService(
        projectors, HighestPriorityStrategy(lambda d: d.get_default_priority_score()))
    print(pj_service.allocate(lambda d: True))

    header("6. Điều hòa tương thích phòng A203")
    ac_service = AllocationService(acs, FirstAvailableStrategy())
    print(ac_service.allocate(lambda d: d.is_compatible_with("A203")))

    header("7. Micro: FirstAvailable")
    mic_service = AllocationService(mics, FirstAvailableStrategy())
    m1 = mic_service.allocate(lambda d: True)
    print(m1)
    m1.return_device()  # trả về kho để thử chiến lược khác

    header("8. Đổi chiến lược lúc chạy")
    mic_service.change_strategy(HighestPriorityStrategy(lambda d: d.get_default_priority_score()))
    m2 = mic_service.allocate(lambda d: True)
    print(f"HighestPriority -> {m2} (điểm {m2.get_default_priority_score()})")

    header("9. Không có ứng viên phù hợp")
    try:
        ac_service.allocate(lambda d: d.is_compatible_with("Z999"))
    except NoSuitableItemException as ex:
        print(f"Bắt được NoSuitableItemException: {ex}")

    header("10. Thiết bị được chọn chuyển sang Borrowed")
    print(f"{m2.id}: {m2.status.value}")
    print(f"Cấp lại với cùng điều kiện sẽ chọn thiết bị khác: {mic_service.allocate(lambda d: True).id}")

    header("11. Repository generic dùng cho 3 loại thiết bị")
    print(f"InMemoryRepository[ProjectorRemote]: {len(projectors.get_all())}")
    print(f"InMemoryRepository[AirConditionerRemote]: {len(acs.get_all())}")
    print(f"InMemoryRepository[WirelessMicrophone]: {len(mics.get_all())}")
    print("-> Cùng một lớp InMemoryRepository, không sao chép mã.")


if __name__ == "__main__":
    main()
