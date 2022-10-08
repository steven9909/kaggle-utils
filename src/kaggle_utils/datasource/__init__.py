from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def check_if_exists(self):
        pass
