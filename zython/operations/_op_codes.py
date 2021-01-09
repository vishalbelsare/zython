import enum


class _Op_code(enum.Enum):
    add = enum.auto()
    sub = enum.auto()
    eq = enum.auto()
    ne = enum.auto()
    lt = enum.auto()
    gt = enum.auto()
    le = enum.auto()
    ge = enum.auto()
    invert = enum.auto()
    xor = enum.auto()
    and_ = enum.auto()
    or_ = enum.auto()
    mul = enum.auto()
    truediv = enum.auto()
    floordiv = enum.auto()
    mod = enum.auto()
    pow = enum.auto()
    alldifferent = enum.auto()
    forall = enum.auto()  # 3 params: (seq, iter_var=None, func=None)
    exists = enum.auto()  # 3 params: (seq, iter_var=None, func=None)
    sum_ = enum.auto()    # 3 params: (seq, iter_var=None, func=None)
    size = enum.auto()
    circuit = enum.auto()
