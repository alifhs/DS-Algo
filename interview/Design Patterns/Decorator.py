"""
Use Case: Extending Functionality of a Data Processing Pipeline

In a data processing pipeline, you might want to extend the functionality of existing components dynamically.
"""


class DataProcessor:
    def process(self):
        return "Processing data"

class DataProcessorDecorator:
    def __init__(self, processor: DataProcessor):
        self._processor = processor

    def process(self):
        return self._processor.process()

class ValidationDecorator(DataProcessorDecorator):
    def process(self):
        result = self._processor.process()
        return f"Validating data -> {result}"

class LoggingDecorator(DataProcessorDecorator):
    def process(self):
        result = self._processor.process()
        return f"Logging data -> {result}"

# Usage
processor = DataProcessor()
print(processor.process())  # Output: Processing data

processor_with_validation = ValidationDecorator(processor)
print(processor_with_validation.process())  # Output: Validating data -> Processing data

processor_with_logging = LoggingDecorator(processor_with_validation)
print(processor_with_logging.process())  # Output: Logging data -> Validating data -> Processing data
