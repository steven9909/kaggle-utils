from pathlib import Path
from typing import Iterator, Tuple

from kaggle_utils.datasource.type.image import IImage


class IImageClassification(IImage):
    def iter_images_and_labels(self) -> Iterator[Tuple[Path, str]]:
        raise NotImplementedError()
