from typing import Any


class Example:
    
    def __init__(self) -> None:
        print('Instance created')

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('Instance called')


object = Example()

object()
