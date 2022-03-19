from abc import ABC, abstractmethod
from typing import (
    Generic,
    Hashable,
    Iterator,
    Optional,
    Tuple,
    TypeVar,
)

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class Face(Generic[K, V], ABC):
    """Base class for post interfaces.

    Params:
        K (Hashable): Type of post identifier.
        V: Type of post data.
    """

    @abstractmethod
    def scrap(self, limit: Optional[int] = None) -> Iterator[Tuple[K, V]]:
        """Scraps existing posts.

        Args:
            limit (Optional[int] = None): How many posts to scrap at maximum.
                If None, scrap all existing posts. Defaults to None.

        Returns:
            Iterator[Tuple[K, V]]: Iterator of post identifier and post data.
        """
        pass

    @abstractmethod
    def post(self, data: V) -> K:
        """Creates new post with given data and get post identifier.

        Args:
            data (V): Post's data.

        Returns:
            K: Identifier of created post.
        """
        pass

    @abstractmethod
    def score(self, post_id: K) -> float:
        """Gets score of a post with given post_id.

        The range for returned score values is not specified.

        Args:
            post_id (K): Identifier of an existing post.

        Returns:
            float: Score of a post.
        """
        pass
