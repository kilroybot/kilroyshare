from abc import ABC, abstractmethod
from typing import Generic, Hashable, Iterator, Optional, Tuple, TypeVar

from kilroyshare.post import PostData

T = TypeVar('T', bound=Hashable)


class KilroyFace(Generic[T], ABC):
    """KilroyFace base class.

    Params:
        T (Hashable): Type of post id.
    """

    @abstractmethod
    def scrap(
            self,
            limit: Optional[int] = None
    ) -> Iterator[Tuple[T, PostData]]:
        """Scraps existing posts.

        Args:
            limit (Optional[int] = None): How many posts to scrap at maximum.
                If None, scrap all existing posts. Defaults to None.

        Returns:
            Iterator[Tuple[T, PostData]]: Iterator of post id and post data.
        """
        return NotImplemented

    @abstractmethod
    def post(self, data: PostData) -> T:
        """Creates new post with given data and get post id.

        Args:
            data (PostData): Post's data.

        Returns:
            T: Id of created post.
        """
        return NotImplemented

    @abstractmethod
    def score(self, post_id: T) -> float:
        """Gets score of a post with given post_id.

        The range for returned score values is not specified.

        Args:
            post_id (T): Id of a post.

        Returns:
            float: Score of a post.
        """
        return NotImplemented
