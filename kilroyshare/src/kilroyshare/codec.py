from abc import ABC, abstractmethod
from typing import Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")


class Codec(ABC, Generic[A, B]):
    """Base class for codecs.

    Params:
        A: Type of data before encoding.
        B: Type of data after encoding.
    """

    @abstractmethod
    def encode(self, value: A) -> B:
        """Encode value.

        Args:
            value (A): Data to encode.

        Returns:
            B: Encoded data.
        """
        pass

    @abstractmethod
    def decode(self, value: B) -> A:
        """Decode value.

        Args:
            value (B): Data to decode.

        Returns:
            A: Decoded data.
        """
        pass
