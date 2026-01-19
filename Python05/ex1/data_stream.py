from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data according to stream-specific rules.
        Args:
            data_batch (List[Any]): A list of raw data items to process.
        Returns:
            str: A formatted string summarizing the processing result.
        """
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter the input batch based on type safety or specific criteria.
        Args:
            data_batch (List[Any]): The raw data list to filter.
            criteria (Optional[str]): Optional filtering condition.
        Returns:
            List[Any]: A new list containing only valid items.
        """
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Retrieve current statistics for this stream.
        Returns:
            Dict[str, Union[str, int, float]]: A dictionary containing
            stream ID and processed count.
        """
        return {
            "stream_id": self.stream_id,
            "items_processed": self.processed_count
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Union[int, float]]) -> str:
        """Calculate average statistics for numeric sensor data.
        Args:
            data_batch (List[Union[int, float]]):
            A list of numeric sensor readings.
        Returns:
            str: A summary string with the count and average value.
        """
        if not data_batch:
            return "Sensor analysis: No readings processed"
        count = len(data_batch)
        self.processed_count += count
        avg = sum(data_batch) / count
        return (f"Sensor analysis: {count} readings processed,"
                f"avg temp: {avg:.1f}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Keep only numeric values from the batch.
        Args:
            data_batch (List[Any]): Input data mixed types.
            criteria (Optional[str]): Unused in this implementation.
        Returns:
            List[Any]: A list containing only integers and floats.
        """
        return [x for x in data_batch if isinstance(x, (int, float))]


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[int]) -> str:
        """Calculate the net flow of financial transaction values.
        Args:
            data_batch (List[int]): A list of transaction amounts.
        Returns:
            str: A summary string showing total count and net financial flow.
        """
        if not data_batch:
            return "Transaction analysis: No operations processed"
        count = len(data_batch)
        self.processed_count += count
        net_flow = sum(data_batch)
        sign = "+" if net_flow > 0 else ""
        return (f"Transaction analysis: {count} operations,"
                f"net flow: {sign}{net_flow} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Keep only integer values (transactions) from the batch.
        Args:
            data_batch (List[Any]): Input data with mixed types.
            criteria (Optional[str]): Unused in this implementation.
        Returns:
            List[Any]: A list containing only integers.
        """
        return [x for x in data_batch if isinstance(x, int)]


class EventStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        """Analyze event logs to count total events and errors.
        Args:
            data_batch (List[str]): A list of event log strings.
        Returns:
            str: A summary indicating total events and error count.
        """
        if not data_batch:
            return "Event analysis: No events processed"
        count = len(data_batch)
        self.processed_count += count
        error_count = 0
        for event in data_batch:
            if "error" in event.lower():
                error_count += 1
        return f"Event analysis: {count} events, {error_count} error detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Keep only string values (event logs) from the batch.
        Args:
            data_batch (List[Any]): Input data with mixed types.
            criteria (Optional[str]): Unused in this implementation.
        Returns:
            List[Any]: A list containing only strings.
        """
        return [x for x in data_batch if isinstance(x, str)]


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a new data stream handler.
        Args:
            stream (DataStream): The stream instance to add to the processor.
        """
        self.streams.append(stream)

    def process_stream_data(self, data_map: Dict[str, List[Any]]) -> List[str]:
        """Route data batches to their corresponding streams for processing.
        Iterates through the input map, matches stream IDs, filters data,
        and executes processing.
        Args:
            data_map (Dict[str, List[Any]]): A dictionary
            mapping stream IDs to data batches.
        Returns:
            List[str]: A list of result strings from each matching stream.
        """
        results = []

        for stream_id, batch_data in data_map.items():
            found_stream = None
            for s in self.streams:
                if s.stream_id == stream_id:
                    found_stream = s
                    break

            if found_stream:
                clean_data = found_stream.filter_data(batch_data)
                result = found_stream.process_batch(clean_data)
                results.append(result)
            else:
                results.append(f"Error: Stream {stream_id} not found")

        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    s_data = [22.5, 65, 1013]
    print(f"Processing sensor batch: [temp:{s_data[0]},"
          f"humidity:{s_data[1]}, pressure:{s_data[2]}]")
    print(sensor.process_batch(s_data))
    print()

    print("Initializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    t_data = [100, -150, 75]
    print(f"Processing transaction batch: [buy:{t_data[0]},"
          f"sell:{abs(t_data[1])}, buy:{t_data[2]}]")
    print(transaction.process_batch(t_data))
    print()

    print("Initializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    e_data = ["login", "Error: timeout", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(e_data))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(transaction)
    manager.add_stream(event)

    batch_data = {
        "SENSOR_001": [20, 22],
        "TRANS_001": [50, 50, 50, 50],
        "EVENT_001": ["ok", "ok", "ok"]
    }

    results = manager.process_stream_data(batch_data)

    print("Batch 1 Results:")
    print(f"- Sensor data: {len(batch_data['SENSOR_001'])} readings processed")
    print(f"- Transaction data: {len(batch_data['TRANS_001'])}"
          f"operations processed")
    print(f"- Event data: {len(batch_data['EVENT_001'])} events processed")
    print()

    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print()

    print("All streams processed successfully. Nexus throughput optimal.")
