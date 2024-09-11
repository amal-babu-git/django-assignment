class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def __iter__(self):
        """Make the class iterable, returning length first, then width."""
        # Use a tuple containing the length and width in the desired format
        self._data = iter([{'length': self.length}, {'width': self.width}])
        return self

    def __next__(self):
        """Return the next value in the iteration."""
        return next(self._data)



rect = Rectangle(10, 5)

# Iterating over the instance of Rectangle
for dimension in rect:
    print(dimension)
