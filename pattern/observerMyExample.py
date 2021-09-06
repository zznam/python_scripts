from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class BuildingManager(Subject):
    #level of emergency
    _level: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("BuildingManager: Notifying all devices...")
        for observer in self._observers:
            observer.update(self)

    def startWarningMode(self, level) -> None:
        print("Emergency: There's an accident happening.".upper())
        self._level = level
        print(f"Emergency level has just changed to: {self._level}".upper())
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class FireAlarm(Observer):
    def update(self, subject: Subject) -> None:
        print("FireAlarm: do ring at level", subject._level)


class EmergencyLight(Observer):
    def update(self, subject: Subject) -> None:
        print("EmergencyLight: turn on light at level", subject._level)


if __name__ == "__main__":

    subject = BuildingManager()

    fireAlarm = FireAlarm()
    subject.attach(fireAlarm)

    emergencyLight = EmergencyLight()
    subject.attach(emergencyLight)

    subject.startWarningMode(3)
    subject.startWarningMode(4)

    #if we don't want to notify a device, detach it
    subject.detach(emergencyLight)

    subject.startWarningMode(5)