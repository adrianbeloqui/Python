
class Vector2d:
    def __init__(self, x_coord, y_coord):
        self.x = float(x_coord)
        self.y = float(y_coord)

    def __str__(self):
        """
        User representation
        """
        return str(tuple(self))

    def __repr__(self):
        """
        Developer representation
        """
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __iter__(self):
        return (i for i in (self.x, self.y))
