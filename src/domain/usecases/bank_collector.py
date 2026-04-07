from abc import ABC, abstractmethod
from typing import Dict, List

class BankCollectorInterface(ABC):

    @abstractmethod
    def list(self) -> List[Dict]:
        raise Exception("Should be implemented in subclass")