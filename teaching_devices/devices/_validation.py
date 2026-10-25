
def require_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} không hợp lệ.")
    return value.strip()


def require_percent(value: int, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= 100:
        raise ValueError(f"{name} phải là số nguyên trong [0, 100].")
    return value
