from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from data_generator.generated_data.alien_contacts import ALIEN_CONTACTS
from datetime import datetime
import random


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation_rules(self) -> AlienContact:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) must include a received message")
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 40)
    random_data = random.choice(ALIEN_CONTACTS)
    try:
        alien_contact = AlienContact(**random_data)
        print(
            "Valid contact report:\n"
            f"ID: {alien_contact.contact_id}\n"
            f"Type: {alien_contact.contact_type.value}\n"
            f"Location: {alien_contact.location}\n"
            f"Signal: {alien_contact.signal_strength}/10\n"
            f"Duration: {alien_contact.duration_minutes} minutes\n"
            f"Witnesses: {alien_contact.witness_count}\n"
            f"Message: '{alien_contact.message_received}'"
        )

    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].replace('Value error, ', '')}")

    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_BAD_002",
            timestamp="2024-05-21T01:00:00",
            location="Bedroom",
            contact_type="telepathic",
            witness_count=1,
            signal_strength=2.0,
            duration_minutes=10,
            is_verified=False
        )
        print(invalid_contact.contact_id)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].replace('Value error, ', '')}")


if __name__ == "__main__":
    main()
