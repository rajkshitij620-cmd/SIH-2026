from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Optional, Any

class RegisterInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)

class LoginInput(BaseModel):
    email: EmailStr
    password: str = Field(max_length=72)

class ResetPasswordInput(BaseModel):
    email: EmailStr
    new_password: str = Field(min_length=6, max_length=72)

class TripInput(BaseModel):
    destination: str = Field(min_length=2)
    budget: int = Field(ge=1000, le=1000000)
    days: int = Field(default=1, ge=1, le=14)
    travellers: int = Field(ge=1)
    traveller_type: str = 'Family'
    gender: Optional[str] = Field(default=None, pattern='^(male|female|other)$')
    age: Optional[int] = Field(default=None, ge=18, le=120)
    interests: List[str] = []
    language: str = 'en'
    preferences: List[str] = []
    start_date: str = Field(min_length=10, max_length=10)
    end_date: str = Field(min_length=10, max_length=10)
    travel_type: str = Field(pattern='^(single|group)$')
    connection_option: Optional[str] = Field(default=None, pattern='^(single_travelling|connect_people)$')
    trip_photo: Optional[str] = Field(default=None, max_length=6_000_000)
    group_member_photos: List[str] = Field(default_factory=list, max_length=10)
    current_location_city: Optional[str] = Field(default=None, max_length=100)
    current_location_latitude: Optional[float] = Field(default=None, ge=-90, le=90)
    current_location_longitude: Optional[float] = Field(default=None, ge=-180, le=180)

    @model_validator(mode='after')
    def valid_trip_dates(self):
        if self.end_date < self.start_date:
            raise ValueError('End date must be on or after start date')
        if self.trip_photo and not self.trip_photo.startswith(('data:image/jpeg;base64,', 'data:image/png;base64,')):
            raise ValueError('Trip photo must be a JPEG, JPG, or PNG image')
        if self.group_member_photos and (len(self.group_member_photos) != self.travellers or any(not photo.startswith(('data:image/jpeg;base64,', 'data:image/png;base64,')) for photo in self.group_member_photos)):
            raise ValueError('Each group member must have a JPEG, JPG, or PNG photo')
        return self

class ChatInput(BaseModel):
    message: str = Field(min_length=2, max_length=1000)
    language: str = 'en'

class ConnectionDecision(BaseModel):
    action: str = Field(pattern='^(accept|decline)$')

class GroupInput(BaseModel):
    trip_id: str
    name: str = Field(min_length=2, max_length=80)
    member_ids: List[str] = []

class GroupMessageInput(BaseModel):
    message: str = Field(min_length=1, max_length=1000)
