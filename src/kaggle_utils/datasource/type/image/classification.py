from pathlib import Path
from typing import Iterator

from kaggle_utils.datasource.type.image import IImage


class IImageClassification(IImage):
    def iter_images_and_labels(self) -> Iterator[Path, str]:
        raise NotImplementedError()
