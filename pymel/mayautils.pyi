from typing import *
from _typeshed import Incomplete
from builtins import str
from typing import Any

sep: Incomplete

def source(file: Any, searchPath: Iterable[str] = ..., recurse: bool = ...) -> None: ...
def getMayaLocation(version: bool = ...) -> Optional[str]: ...
def getMayaAppDir(versioned: bool = ...) -> Optional[str]: ...
def getUserPrefsDir() -> Optional[str]: ...
def getUserScriptsDir() -> Optional[str]: ...
def executeDeferred(func, *args, **kwargs) -> None: ...
def recurseMayaScriptPath(roots: Union[str, List[str], Tuple[str]] = ..., verbose: bool = ..., excludeRegex: str = ..., errors: Any = ..., prepend: Any = ...) -> None: ...