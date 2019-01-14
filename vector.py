from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __str__(self):
        """
        User representation
        """
        return str(tuple(self))

    def __repr__(self):
        """
        Developer representation
        """
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        class_name = type(self).__name__
        return "{}({})".format(class_name, components)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec):
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self), self.angles()])
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def __iter__(self):
        return iter(self._components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return len(self) != len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        elif isinstance(index, tuple):
            results = list()
            for s in index:
                results.append(self[s])
            return results
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, item))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)
