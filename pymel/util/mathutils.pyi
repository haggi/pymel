from typing import *
from typing import Any

def conjugate(x): ...
def real(x): ...
def imag(x): ...
def round(value, ndigits: int = ...): ...
def gamma(c: Any, g: Any) -> float: ...
def blend(a: Any, b: Any, weight: Any = ...) -> float: ...
def smoothmap(min: Any, max: Any, x: Any) -> float: ...
def smoothstep(min: Any, max: Any, x: Any) -> float: ...
def linmap(min: Any, max: Any, x: Any) -> float: ...
def linstep(min: Any, max: Any, x: Any) -> float: ...
def clamp(x: Any = ..., min: Any = ..., max: Any = ...) -> float: ...
def setRange(x: Any = ..., oldmin: Any = ..., oldmax: Any = ..., newmin: Any = ..., newmax: Any = ...) -> float: ...
def hermiteInterp(x: Any = ..., y0: Any = ..., y1: Any = ..., s0: Any = ..., s1: Any = ...) -> float: ...
def hermite(x: Any = ..., v0: Any = ..., v1: Any = ..., s0: Any = ..., s1: Any = ...) -> float: ...