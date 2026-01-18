from data_generator.generated_data.space_stations import SPACE_STATIONS
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import random


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main():
    random_data = random.choice(SPACE_STATIONS)
    try:
        station = SpaceStation(**random_data)
        print(
            "Valid station created successfully:\n"
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level}%\n"
            f"Oxygen: {station.oxygen_level}%"
        )
        status = "Operational" if station.is_operational else "Non-Operational"
        print(f"Status: {status}")
        if station.notes:
            print(f"Notes: {station.notes}")

    except ValidationError as e:
        print("\nValidation Failed!")
        for error in e.errors():
            print(f"- Field '{error['loc'][0]}': {error['msg']}")

    print()
    print("=" * 40)
    print("Test with intentionally invalid data:")
    try:
        bad_station = SpaceStation(
            station_id="X",
            name="Test",
            crew_size=100,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime(2023, 1, 1)
        )
        print(bad_station.station_id)
    except ValidationError as e:
        for error in e.errors():
            print(f"- Field '{error['loc'][0]}': {error['msg']}")


if __name__ == "__main__":
    main()
