from abc import ABC, abstractmethod

class CompylerPlugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
        
    @property
    @abstractmethod
    def version(self) -> str:
        pass
        
    @abstractmethod
    def initialize(self, compiler):
        pass
        
    @abstractmethod
    def pre_compile(self, source_file):
        pass
        
    @abstractmethod
    def post_compile(self, output_file):
        pass
