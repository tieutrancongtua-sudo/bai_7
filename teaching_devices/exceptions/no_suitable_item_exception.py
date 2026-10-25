class NoSuitableItemException(Exception):
    def __init__(self):
        super().__init__("Không có thiết bị phù hợp.")
