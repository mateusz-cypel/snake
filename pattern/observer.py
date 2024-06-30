from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    """The Subject interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        raise NotImplemented()

    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        raise NotImplemented()

    def notify(self) -> None:
        """Notify all observers about an event."""
        raise NotImplemented()


class Observer(ABC):
    """The Observer interface declares the update method, used by subjects."""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Receive update from subject."""
        raise NotImplemented()


