from collections import deque
from enum import Enum


class BadFormattedCodeString(Exception):
    pass


class Direction(Enum):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'


class CharType(Enum):
    BRACKET = 'BRACKET'
    PARENTHESES = 'PARENTHESES'
    OTHER = 'OTHER'


class CodeFormatValidator:

    def __init__(self, code_string: str) -> None:
        self.code_string = code_string
        self.brackets_stack = deque()
        self.parentheses_stack = deque()
        self.first_char_type = self.__get_first_opening_char_type()

    def __get_first_opening_char_type(self) -> CharType:
        """Return what type of char is opnening the code block."""
        if not self.code_string:
            raise ValueError('Code string must not be empty.')
        chars = self.code_string.split()
        
        while chars:
            char = chars.pop(0)
            type_ = self.__get_char_type(char)
            if type_ is not CharType.OTHER:
                return type_
        
        raise ValueError('Value is not a code string.')

    def __get_direction(self, char: str) -> Direction:
        """Return if code char is opening or closing a code block."""
        if char in ('{', '('):
            return Direction.OPEN
        if char in ('}', ')'):
            return Direction.CLOSE
        raise ValueError('Not a open/close code character.')

    def __get_char_type(self, char: str) -> CharType:
        """Return the type of the char (Bracket, parentheses or other)."""
        if char in ('{', '}'):
            return CharType.BRACKET
        if char in ('(', ')'):
            return CharType.PARENTHESES
        return CharType.OTHER

    def has_valid_format(self) -> bool:
        """Validate the provided code string format."""
        characters = self.code_string.split()

        while characters:
            char: str = characters.pop(0)
            char_type = self.__get_char_type(char)
            if char_type is not CharType.OTHER:
                try:
                    self.__move_stacks(char)
                except BadFormattedCodeString:
                    return False

        return not characters

    def __move_stacks(self, char: str) -> None:
        """Validate the next opening/close code block char."""
        direction = self.__get_direction(char)
    
        if char is CharType.BRACKET:

            if self.__get_direction(char) is Direction.OPEN:
                self.brackets_stack.append('.')
            elif self.__get_direction(char) is Direction.CLOSE:
                self.brackets_stack.pop()
                self.__validate_removal(CharType.BRACKET)

        elif char is CharType.PARENTHESES:

            if self.__get_direction(char) is Direction.OPEN:
                self.parentheses_stack.append('.')
            elif self.__get_direction(char) is Direction.CLOSE:
                self.parentheses_stack.pop()
                self.__validate_removal(CharType.PARENTHESES)

    def __validate_removal(self, char_type: CharType) -> None:
        if char_type is self.first_char_type:
            if (
                char_type is CharType.BRACKET
                and
                self.parentheses_stack > self.brackets_stack
            ):
                raise BadFormattedCodeString()
            if (
                char_type is CharType.PARENTHESES
                and
                self.brackets_stack > self.parentheses_stack
            ):
                raise BadFormattedCodeString()
