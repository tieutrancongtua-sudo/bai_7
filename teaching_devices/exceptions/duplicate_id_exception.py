class DuplicateIdException(Exception):
    def __init__(self, duplicate_id: str):
        super().__init__(f"Mã '{duplicate_id}' đã tồn tại.")
        self.duplicate_id = duplicate_id
