class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException("Нельзя так делать")



sq1 = Square(-3)
