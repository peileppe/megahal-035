from megahal.megahal import (
    DEFAULT_BANWORDS, DEFAULT_ORDER, DEFAULT_TIMEOUT, Brain, Dictionary,
    MegaHAL, Tree,
)

__version__ = "0.4.0"
VERSION = tuple(map(int, __version__.split(".")))

__all__ = ["Brain", "DEFAULT_BANWORDS", "DEFAULT_ORDER", "DEFAULT_TIMEOUT", "Dictionary", "MegaHAL", "Tree"]
