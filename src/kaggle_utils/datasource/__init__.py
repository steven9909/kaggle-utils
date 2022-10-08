from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def check_exists(self):
        """
        Check if the datasource exists locally or remotely
        """

        raise NotImplementedError()
