from abc import ABC, abstractmethod
from typing import (
    AsyncIterator,
    Generic,
    Hashable,
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
    async def scrap(
        self, limit: Optional[int] = None
    ) -> AsyncIterator[Tuple[K, V]]:
        """Scraps existing posts.

        Args:
            limit (Optional[int] = None): How many posts to scrap at maximum.
                If None, scrap all existing posts. Defaults to None.

        Returns:
            AsyncIterator[Tuple[K, V]]: Async iterator of post identifier and
                post data.
        """
        pass

    @abstractmethod
    async def post(self, data: V) -> K:
        """Creates new post with given data and get post identifier.

        Args:
            data (V): Post's data.

        Returns:
            K: Identifier of created post.
        """
        pass

    @abstractmethod
    async def score(self, post_id: K) -> float:
        """Gets score of a post with given post_id.

        The range for returned score values is not specified.

        Args:
            post_id (K): Identifier of an existing post.

        Returns:
            float: Score of a post.
        """
        pass
