# Project - Implementing FCFS Algorithm using Queues
# Adapted from QueueInterface.java

# ABC and abstractmethod used to mimic Java's 'interface' behaviour
from abc import ABC, abstractmethod

# TypeVar and Generic used to mimic Java's '<T>' syntax
from typing import TypeVar, Generic

# Defines T as a TypeVar for generics
T = TypeVar('T')

#Represents a generic queue interface
class QueueInterface(ABC, Generic[T]):

    @abstractmethod
    def enqueue(self, newEntry) -> None:
        """Adds a new entry to the back of the queue"""
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """
        Removes and returns the entry at the front of the queue
        :raises IndexError: if the queue is empty
        """
        pass

    @abstractmethod
    def get_front(self) -> T:
        """
        Retrieves the entry at the front of the queue
        :raises IndexError: if the queue is empty
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Checks whether the queue is empty"""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Removes all entries from the queue"""
        pass
