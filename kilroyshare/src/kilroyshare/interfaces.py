from abc import ABC, abstractmethod
from typing import Hashable, TypeVar, Generic

from kilroyshare.post import PostData

T = TypeVar('T', bound=Hashable)


class KilroyFace(Generic[T], ABC):
    """
    KilroyFace base class.

    Params:
        T (Hashable): Type of post id.
    """

    @abstractmethod
    def post(self, data: PostData) -> T:
        """
        Create new post with given data and get post id.

        Args:
            data (PostData): Post's data.

        Returns:
            T: Id of created post.
        """
        return NotImplemented

    @abstractmethod
    def score(self, post_id: T) -> float:
        """
        Get score of a post with given post_id.
        The range for returned score values is not specified.

        Args:
            post_id (T): Id of a post.

        Returns:
            float: Score of a post.
        """
        return NotImplemented
