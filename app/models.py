from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class MoodEntry:
    date: str = field(default_factory=lambda: datetime.today().strftime('%Y-%m-%d'))
    mood: int = 0
    notes: str = ""

@dataclass
class CBTEntry:
    date: str = field(default_factory=lambda: datetime.today().strftime('%Y-%m-%d'))
    thought: str = ""
    ai_response: Optional[str] = None


@dataclass
class CheckInEntry:
    date: str = field(default_factory=lambda: datetime.today().strftime('%Y-%m-%d'))
    mood: int = 0
    notes: str = ""
@dataclass
class UserData:
    moods: List[MoodEntry] = field(default_factory=list)
    cbt_sessions: List[CBTEntry] = field(default_factory=list)
    checkins: List[CheckInEntry] = field(default_factory=list)
    def __post_init__(self):
        self.moods = self.moods or []
        self.cbt_sessions = self.cbt_sessions or []
        self.checkins = self.checkins or []