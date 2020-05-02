from megahal.megahal import (
    DEFAULT_BANWORDS, DEFAULT_BRAINFILE, DEFAULT_ORDER, DEFAULT_TIMEOUT,
    Brain, Dictionary, MegaHAL, Tree,
)


__version__ = "0.3.5"
VERSION = tuple(map(int, __version__.split(".")))

__all__ = [
    "MegaHAL", "Dictionary", "Tree", "__version__", "DEFAULT_ORDER", "Brain",
    "DEFAULT_BRAINFILE", "DEFAULT_BANWORDS", "DEFAULT_TIMEOUT",
]
