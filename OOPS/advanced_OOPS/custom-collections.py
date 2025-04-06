from typing import List, Dict, Any, Iterator, Protocol, TypeVar, Generic, Optional
from collections.abc import MutableSequence, Mapping
import bisect
import copy

T = TypeVar('T')  # Generic type for our collections

class Comparable(Protocol):
    """A protocol defining objects that can be compared."""
    def __lt__(self, other: Any) -> bool:
        """Less than comparison."""
        ...

class SortedList(MutableSequence[T]):
    """
    A list that maintains its elements in sorted order.
    Demonstrates subclassing from collections.abc for proper collection behavior.
    """
    def __init__(self, iterable=None):
        self._data: List[T] = []
        if iterable is not None:
            self.extend(iterable)
    
    def __getitem__(self, index):
        """Get item at index."""
        return self._data[index]
    
    def __setitem__(self, index, value):
        """Prohibit direct setting of items."""
        raise NotImplementedError("Cannot set items directly in a SortedList")
    
    def __delitem__(self, index):
        """Delete item at index."""
        del self._data[index]
    
    def __len__(self):
        """Return the number of items."""
        return len(self._data)
    
    def insert(self, index, value):
        """Insert value at the correct position to maintain order."""
        # Ignore index and insert at the correct position
        bisect.insort(self._data, value)
    
    def __repr__(self):
        return f"SortedList({self._data})"
    
    def __str__(self):
        return str(self._data)

class LRUCache(Mapping[str, T]):
    """
    A Least Recently Used (LRU) cache implementation.
    Demonstrates a custom mapping type with eviction policy.
    """
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self._cache: Dict[str, T] = {}
        self._usage_order: List[str] = []  # Keys ordered by usage (newest at end)
    
    def __getitem__(self, key: str) -> T:
        """Get an item and mark it as recently used."""
        if key not in self._cache:
            raise KeyError(key)
        
        # Update usage order
        self._usage_order.remove(key)
        self._usage_order.append(key)
        
        return self._cache[key]
    
    def __setitem__(self, key: str, value: T) -> None:
        """Set an item and mark it as recently used."""
        if key in self._cache:
            # Update existing key
            self._usage_order.remove(key)
        elif len(self._cache) >= self.capacity:
            # Evict least recently used item
            lru_key = self._usage_order.pop(0)
            del self._cache[lru_key]
        
        # Add new item
        self._cache[key] = value
        self._usage_order.append(key)
    
    def __delitem__(self, key: str) -> None:
        """Remove an item from the cache."""
        if key not in self._cache:
            raise KeyError(key)
        
        del self._cache[key]
        self._usage_order.remove(key)
    
    def __iter__(self) -> Iterator[str]:
        """Iterate over keys in usage order."""
        return iter(self._usage_order)
    
    def __len__(self) -> int:
        """Return the number of items in the cache."""
        return len(self._cache)
    
    def __repr__(self) -> str:
        items = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"LRUCache({{{items}}})"

class Observable(Generic[T]):
    """
    A generic observable value container with change notifications.
    Demonstrates the observer pattern with generics.
    """
    def __init__(self, initial_value: T):
        self._value = initial_value
        self._observers = []
    
    @property
    def value(self) -> T:
        """Get the current value."""
        return copy.deepcopy(self._value)  # Return a copy to prevent modification
    
    @value.setter
    def value(self, new_value: T) -> None:
        """Set a new value and notify observers."""
        if self._value != new_value:
            old_value = self._value
            self._value = new_value
            self._notify(old_value, new_value)
    
    def add_observer(self, callback) -> None:
        """Add an observer callback."""
        if callback not in self._observers:
            self._observers.append(callback)
    
    def remove_observer(self, callback) -> None:
        """Remove an observer callback."""
        if callback in self._observers:
            self._observers.remove(callback)
    
    def _notify(self, old_value: T, new_value: T) -> None:
        """Notify all observers of a value change."""
        for callback in self._observers:
            callback(old_value, new_value)

class TreeNode(Generic[T]):
    """
    A generic binary tree node implementation.
    Demonstrates recursive data structures with generics.
    """
    def __init__(self, value: T):
        self.value = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None
        self.parent: Optional[TreeNode[T]] = None
    
    def insert(self, value: T) -> None:
        """Insert a value into the tree."""
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.parent = self
            else:
                self.right.insert(value)
    
    def search(self, value: T) -> Optional['TreeNode[T]']:
        """Search for a value in the tree."""
        if value == self.value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return None
    
    def inorder_traversal(self) -> List[T]:
        """Perform an inorder traversal of the tree."""
        result = []
        if self.left is not None:
            result.extend(self.left.inorder_traversal())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.inorder_traversal())
        return result
    
    def __repr__(self) -> str:
        return f"TreeNode({self.value})"

# Using the custom collections
print("\n---- SortedList Demo ----")
sorted_list = SortedList([5, 2, 8, 1, 9])
print(f"Initial list: {sorted_list}")

sorted_list.append(4)
print(f"After append(4): {sorted_list}")

sorted_list.extend([7, 3, 6])
print(f"After extend([7, 3, 6]): {sorted_list}")

try:
    sorted_list[2] = 10  # Should raise NotImplementedError
except NotImplementedError as e:
    print(f"Expected error: {e}")

print(f"Get item at index 3: {sorted_list[3]}")
print(f"Slice [2:5]: {sorted_list[2:5]}")

print("\n---- LRUCache Demo ----")
cache = LRUCache(capacity=3)
cache["key1"] = "value1"
cache["key2"] = "value2"
cache["key3"] = "value3"

print(f"Cache after adding 3 items: {cache}")
print(f"Get 'key1': {cache['key1']}")  # Should move key1 to most recently used

# This should evict key2 (least recently used)
cache["key4"] = "value4"
print(f"Cache after adding 'key4': {cache}")

try:
    # key2 should be evicted
    print(cache["key2"])
except KeyError:
    print("Expected: key2 was evicted")

print("\n---- Observable Demo ----")
def value_changed(old_value, new_value):
    print(f"Value changed from {old_value} to {new_value}")

observable = Observable(42)
observable.add_observer(value_changed)

observable.value = 100  # Should trigger notification
observable.value = 100  # No change, should not trigger notification
observable.value = 200  # Should trigger notification

print("\n---- Binary Tree Demo ----")
tree = TreeNode(50)
for value in [30, 70, 20, 40, 60, 80, 35]:
    tree.insert(value)

print(f"Inorder traversal: {tree.inorder_traversal()}")
print(f"Search for 40: {tree.search(40)}")
print(f"Search for 55: {tree.search(55)}")  # Should return None