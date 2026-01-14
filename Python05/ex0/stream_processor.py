from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    # @abstractmethod
    def format_output(self, result: str) -> str:
        """Format the output string"""
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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
        return (f"Validation: Numeric data verified\n"
                f"Output: {result}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data.startswith("")
        except AttributeError:
            return False
        else:
            return True

    def process(self, data: Optional[str]) -> str:
        length = len(data)
        words = len(data.split())
        return f"Output: Processed text: {length} characters, {words} words"

    def format_output(self, result: str) -> str:
        return (f"Validation: Text data verified\n"
                f"Output: {result}")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data.items()
        except AttributeError:
            return False
        else:
            return True

    def process(self, data: Union[Dict[str, str], List[str]]) -> str:
        messages = []
        for key, value in data.items():
            messages.append(f"[ALERT] {key} level detected: {value}")
        return "\n".join(messages)

    def format_output(self, result: str) -> str:
        return (f"Validation: Log entry verified\n"
                f"Output: {result}")


# def main() -> None:
#     num_proc = NumericProcessor()
#     txt_proc = TextProcessor()
#     log_proc = LogProcessor()
#
#     all_processors = [num_proc, txt_proc, log_proc]
#
#     print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
#
#     # 1. Numeric
#     print("Initializing Numeric Processor...")
#     data1 = [1, 20, -3, 44, 5]
#     print(f"Processing data: {data1}")
#     if num_proc.validate(data1):
#         res1 = num_proc.process(data1)
#         print(num_proc.format_output(res1))
#     print()
#
#     # 2. Text
#     print("Initializing Text Processor...")
#     data2 = "I know KungFu"
#     print(f"Processing data: \"{data2}\"")
#     if txt_proc.validate(data2):
#         res2 = txt_proc.process(data2)
#         print(txt_proc.format_output(res2))
#     print()
#
#     # 3. Log
#     print("Initializing Log Processor...")
#     data3 = {"404": "Page not found"}
#     print("Processing data: \"ERROR: Connection timeout\"")
#     if log_proc.validate(data3):
#         res3 = log_proc.process(data3)
#         print(log_proc.format_output(res3))
#     print()
#
#     print("=== Polymorphic Processing Demo ===")
#     print("Processing multiple data types through same interface...")
#
#     mixed_data = [
#         [1, 20, -3, 44, 5],
#         "I know KungFu",
#         {"404": "Page not found"}
#     ]
#
#     counter = 1
#
#     for item in mixed_data:
#         for p in all_processors:
#             if p.validate(item):
#                 result = p.process(item)
#                 print(f"Result {counter}: {result}")
#                 counter += 1
#                 break
#     print()
#
#     print("Foundation systems online. Nexus ready for advanced streams.")
#
#
# if __name__ == "__main__":
#     main()
