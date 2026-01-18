from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from data_generator.generated_data.space_missions import SPACE_MISSIONS
import random


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_safety(self) -> SpaceMission:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is not active")
        lieder = any(
            member.rank in (Rank.captain, Rank.commander)
            for member in self.crew
        )
        if not lieder:
            raise ValueError("Mission must have at least"
                             "one Commander or Captain")
        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError("Long missions require at least 50% "
                                 "experienced crew (5+ years)")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 40)
    random_data = random.choice(SPACE_MISSIONS)

    try:
        mission = SpaceMission(**random_data)
        print("Valid mission created:\n"
              f"Mission: {mission.mission_name}\n"
              f"ID: {mission.mission_id}\n"
              f"Destination: {mission.destination}\n"
              f"Duration: {mission.duration_days} days\n"
              f"Budget: ${mission.budget_millions}M\n"
              f"Crew size: {len(mission.crew)}\n"
              "Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg'].replace('Value error, ', '')}")

    print()
    print("=" * 40)
    print("Expected validation error (No Commander):")
    try:
        bad_data = random_data

        bad_data['crew'] = [
            member for member in bad_data['crew']
            if member['rank'] not in ('captain', 'commander')
        ]
        invalid_mission = SpaceMission(**bad_data)
        print(invalid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg'].replace('Value error, ', '')}")


if __name__ == "__main__":
    main()
