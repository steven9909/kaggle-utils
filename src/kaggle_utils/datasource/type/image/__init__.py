from pathlib import Path
from typing import Iterator

from kaggle_utils.datasource.type import DataSourceType


class IImage(DataSourceType):
    def iter_images(self) -> Iterator[Path]:
        raise NotImplementedError()
