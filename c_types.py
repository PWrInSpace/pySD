class CVariable():
    def __init__(self, type: str, name: str):
        self._type = type
        self._name = name

    def __str__(self) -> str:
        return f'{self.type} {self.name}'

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def type(self) -> str:
        return self._type

    @property
    def name(self) -> str:
        return self._name
