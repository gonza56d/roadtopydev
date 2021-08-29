from typing import Any


class Example:
    
    def __init__(self) -> None:
        print('Instance created')

    def __call__(self, how, *args: Any, **kwargs: Any) -> Any:
        print(f'Instance called {how}')


object = Example()

object('fast')
