from pathlib import Path
from typing import Iterator, Protocol


class IImage(Protocol):
    def iter_images(self) -> Iterator[Path]:
        raise NotImplementedError()
