from abc import ABC, abstractmethod
from typing import (
    Collection,
    Dict,
    Generic,
    Hashable,
    Iterator,
    Optional,
    Tuple,
    TypeVar,
)

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class OfflineModule(ABC, Generic[V]):
    """Base class for offline modules.

    Params:
        V: Type of sample.
    """

    @abstractmethod
    def fit(self, samples: Collection[V]) -> Optional[Dict[str, float]]:
        """Accumulate gradients mimicking existing samples.

        Args:
            samples (Collection[V]): Collection of existing samples.

        Returns:
            Optional[Dict[str, float]]: Optional metrics dictionary.
        """
        pass

    @abstractmethod
    def step(self) -> "OfflineModule":
        """Updated parameters with accumulated gradients.

        Returns:
            OfflineModule: Instance of OfflineModule after update (usually
                self).
        """
        pass


class OnlineModule(ABC, Generic[K, V]):
    """Base class for modules.

    Params:
        K (Hashable): Type of internal identifier of generated samples.
        V: Type of sample.
    """

    @abstractmethod
    def sample(self, n: int = 1) -> Iterator[Tuple[K, V]]:
        """Generates new samples.

        Args:
            n (int, default: 1): How many samples to generate.

        Returns:
            Iterator[Tuple[K, V]]: Iterator of tuples with internal identifier
                of generated sample and generated sample itself.
        """
        pass

    @abstractmethod
    def fit(self, scores: Dict[K, float]) -> Optional[Dict[str, float]]:
        """Accumulate gradients from scores of previously generated samples.

        Args:
            scores (Dict[K, float]): Dictionary with internal sample
                identifiers as keys and sample scores as values.

        Returns:
            Optional[Dict[str, float]]: Optional metrics dictionary.
        """
        pass

    @abstractmethod
    def step(self) -> "OnlineModule":
        """Updated parameters with accumulated gradients.

        Returns:
            OnlineModule: Instance of OnlineModule after update (usually self).
        """
        pass
