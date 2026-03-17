class BaseCommonException(Exception):
    message: str

    def __init__(self) -> None:
        super().__init__(self.message)
