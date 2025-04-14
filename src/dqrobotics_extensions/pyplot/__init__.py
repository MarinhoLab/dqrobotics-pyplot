from dqrobotics_extensions.pyplot._pyplot import plot

# https://setuptools-git-versioning.readthedocs.io/en/stable/runtime_version.html
from pathlib import Path
__version__ = Path(__file__).parent.joinpath("VERSION").read_text()