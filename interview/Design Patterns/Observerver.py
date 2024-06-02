"""
Use Case: Event Notification System
In an application where multiple objects need to be notified of changes, like a logging system or an event notification system.
"""

class Subject: 
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject): # can be package-purchase and then log it and email the user, any class will inherit base subject
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter   #decorator
    def state(self, value):
        self._state = value
        self.notify()

class Observer:
    def update(self, subject):
        pass

class LoggingObserver(Observer):
    def update(self, subject):
        print(f"Logging: Subject's state is now {subject.state}")

class EmailObserver(Observer):
    def update(self, subject):
        print(f"Email: Subject's state is now {subject.state}")

# Usage
subject = ConcreteSubject()
logger = LoggingObserver()
emailer = EmailObserver()

subject.attach(logger)
subject.attach(emailer)

subject.state = "New Event"  # Both observers are notified and print the new state
