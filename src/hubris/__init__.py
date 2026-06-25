from importlib.metadata import PackageNotFoundError, version

from .read_params import read_file

try:
    __version__ = version("hubris")
except PackageNotFoundError:  # not installed (e.g. running from a source checkout)
    __version__ = "0.0.0+unknown"

__all__ = ["read_file", "__version__"]
