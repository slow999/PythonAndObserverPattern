# A few drivers are awaiting traffic light.
# Subject is light.
# Observer is driver.

from abc import ABC, abstractmethod
import random


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class TrafficLight(Subject):
    _all_states = ['green', 'yellow', 'red']
    _state = None
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def switch_light(self):
        # Obviously traffic light does not switch randomly in reality.
        self._state = random.choice(self._all_states)
        print(f'Traffic light: turns {self._state}')
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class GoodDriver(Observer):
    def update(self, subject):
        if subject._state == 'green':
            print('Good driver: drive')


class ImpatientDriver(Observer):
    def update(self, subject):
        if subject._state in ['green', 'yellow']:
            print('Impatient driver: drive')


class BadDriver(Observer):
    def update(self, subject):
        if subject._state:
            print('Bad driver: drive')


if __name__ == '__main__':
    # A traffic road
    traffic_light = TrafficLight()

    good_driver1 = GoodDriver()
    good_driver2 = GoodDriver()
    traffic_light.attach(good_driver1)
    traffic_light.attach(good_driver2)

    impatient_driver1 = ImpatientDriver()
    impatient_driver2 = ImpatientDriver()
    traffic_light.attach(impatient_driver1)
    traffic_light.attach(impatient_driver2)

    bad_driver1 = BadDriver()
    traffic_light.attach(bad_driver1)

    traffic_light.switch_light()