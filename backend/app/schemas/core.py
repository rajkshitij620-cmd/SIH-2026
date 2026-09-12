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

class GoogleAuthInput(BaseModel):
    email: EmailStr
    name: Optional[str] = 'Google Explorer'
    avatar_url: Optional[str] = None
    token: Optional[str] = None

class TripInput(BaseModel):
    destination: str = Field(min_length=2)
    budget: int = Field(ge=1000, le=1000000)
    days: Optional[int] = Field(default=1, ge=1, le=14)
    travellers: int = Field(default=1, ge=1)
    traveller_type: str = 'Family'
    gender: Optional[str] = None
    age: Optional[int] = None
    interests: List[str] = []
    language: str = 'en'
    preferences: List[str] = []
    start_date: str = Field(min_length=10, max_length=10)
    end_date: str = Field(min_length=10, max_length=10)
    travel_type: str = 'single'
    connection_option: Optional[str] = None
    trip_photo: Optional[str] = None
    group_member_photos: List[str] = Field(default_factory=list, max_length=10)
    current_location_city: Optional[str] = None
    current_location_latitude: Optional[float] = None
    current_location_longitude: Optional[float] = None

    @model_validator(mode='before')
    @classmethod
    def clean_empty_strings(cls, values):
        if isinstance(values, dict):
            for k in ['gender', 'connection_option', 'trip_photo', 'current_location_city', 'age']:
                if values.get(k) == '' or values.get(k) is None:
                    values[k] = None
            if values.get('travel_type') not in ['single', 'group']:
                values['travel_type'] = 'single'
        return values

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

