import logging


class MyDivision:

    def __init__(self, dividend, divider) -> None:
        self.dividend, self.divider = dividend, divider

    def __enter__(self):
        return self.dividend / self.divider

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is not None:
            logging.error(f'{exc_type} occurred: {exc_value}')


with MyDivision(5, 0) as division:
    print(division)
