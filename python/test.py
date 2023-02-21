from abc import ABC , abstractmethod


class animal(ABC):
    def __animal__():
        pass  

    @abstractmethod
    def make_sound():
        pass

class Lion(animal):

    def make_sound():
        pass

test = Lion()