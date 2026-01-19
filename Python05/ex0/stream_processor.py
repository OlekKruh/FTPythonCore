from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Determine if the provided data is suitable for this
        specific processor.
        Args:
            data (Any): The raw input data to check.
        Returns:
            bool: True if the data is valid for this processor,
            False otherwise.
        """
        ...

    @abstractmethod
    def process(self, data: Any) -> str:
        """Transform the raw input data into a processed result string.
        Args:
            data (Any): The raw input data to be processed.
        Returns:
            str: The processed result string.
        """
        ...

    def format_output(self, result: str) -> str:
        """Apply final formatting to the processed result for display.
        Args:
            result (str): The string result returned by the process method.
        Returns:
            str: The fully formatted output string ready for display.
        """
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Check if data is a list of numeric values.
        Args:
            data (Any): The input data to verify.
        Returns:
            bool: True if data is a list of integers or numbers,
            False otherwise.
        """
        try:
            for fig in data:
                x = int(fig)
                if fig != x:
                    return False
        except (ValueError, TypeError):
            return False
        else:
            return True

    def process(self, data: List[int]) -> str:
        """Calculate sum and average of the provided numeric list.
        Args:
            data (List[int]): A list of integer numbers.
        Returns:
            str: A summary string containing the count, sum, and average.
        """
        fig_sum = 0
        quant = len(data)

        for fig in data:
            fig_sum += fig

        if quant == 0:
            avg = 0
        else:
            avg = fig_sum / quant

        return f"Processed {quant} numeric values, sum={fig_sum}, avg={avg}"

    def format_output(self, result: str) -> str:
        """Apply final formatting to the processed result for display.
        Args:
            result (str): The string result returned by the process method.
        Returns:
            str: The fully formatted output string ready for display.
        """
        return (f"Validation: Numeric data verified\n"
                f"Output: {result}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Check if the input data is a valid string.
        Args:
            data (Any): The input data to verify.
        Returns:
            bool: True if data is a string, False otherwise.
        """
        try:
            data.startswith("")
        except AttributeError:
            return False
        else:
            return True

    def process(self, data: Optional[str]) -> str:
        """Analyze text to count total characters and words.
        Args:
            data (Optional[str]): The input text string to analyze.
        Returns:
            str: A formatted string stating the character and word counts.
        """
        length = len(data)
        words = len(data.split())
        return f"Output: Processed text: {length} characters, {words} words"

    def format_output(self, result: str) -> str:
        """Apply final formatting to the processed result for display.
        Args:
            result (str): The string result returned by the process method.
        Returns:
            str: The fully formatted output string ready for display.
        """
        return (f"Validation: Text data verified\n"
                f"Output: {result}")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Check if the input data is a dictionary structure.
        Args:
            data (Any): The input data to verify.
        Returns:
            bool: True if data allows .items() access (e.g., a dictionary),
            False otherwise.
        """
        try:
            data.items()
        except AttributeError:
            return False
        else:
            return True

    def process(self, data: Union[Dict[str, str], List[str]]) -> str:
        """Format dictionary items into alert messages for the log.
        Args:
            data (Union[Dict[str, str], List[str]]):
            Dictionary of log levels and messages.
        Returns:
            str: A multiline string of formatted log alerts.
        """
        messages = []
        for key, value in data.items():
            messages.append(f"[ALERT] {key} level detected: {value}")
        return "\n".join(messages)

    def format_output(self, result: str) -> str:
        """Apply final formatting to the processed result for display.
        Args:
            result (str): The string result returned by the process method.
        Returns:
            str: The fully formatted output string ready for display.
        """
        return (f"Validation: Log entry verified\n"
                f"Output: {result}")


def main() -> None:
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    all_processors = [num_proc, txt_proc, log_proc]

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # 1. Numeric
    print("Initializing Numeric Processor...")
    data1 = [1, 20, -3, 44, 5]
    print(f"Processing data: {data1}")
    if num_proc.validate(data1):
        res1 = num_proc.process(data1)
        print(num_proc.format_output(res1))
    print()

    # 2. Text
    print("Initializing Text Processor...")
    data2 = "I know KungFu"
    print(f"Processing data: \"{data2}\"")
    if txt_proc.validate(data2):
        res2 = txt_proc.process(data2)
        print(txt_proc.format_output(res2))
    print()

    # 3. Log
    print("Initializing Log Processor...")
    data3 = {"404": "Page not found"}
    print("Processing data: \"ERROR: Connection timeout\"")
    if log_proc.validate(data3):
        res3 = log_proc.process(data3)
        print(log_proc.format_output(res3))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    mixed_data = [
        [1, 20, -3, 44, 5],
        "I know KungFu",
        {"404": "Page not found"}
    ]

    counter = 1

    for item in mixed_data:
        for p in all_processors:
            if p.validate(item):
                result = p.process(item)
                print(f"Result {counter}: {result}")
                counter += 1
                break
    print()

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
