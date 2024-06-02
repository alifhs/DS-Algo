class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'log_file'):
            self.log_file = "app.log"

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

# Usage
logger1 = Logger()
logger2 = Logger()

logger1.log("This is the first log message.")
logger2.log("This is the second log message.")

print(logger1 is logger2)  # Output: True

# Check log file to see the messages
with open("app.log", "r") as file:
    print(file.read())
