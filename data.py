from datetime import datetime
from dataclasses import dataclass


@dataclass
class String:
    fr: str
    en_maybe: str
    
    @property
    def en(self):
        return self.en_maybe if self.en_maybe else self.fr
    
    
@dataclass
class CompleteDate:
    date: datetime
    
    @property
    def fr(self):
        return self.date.strftime("%d %B %Y")
    @property
    def en(self):
        return self.date.strftime("%B %d %Y")


@dataclass
class Date:
    date: datetime
    
    @property
    def fr(self):
        return self.date.strftime("%d %b %Y")
    @property
    def en(self):
        return self.date.strftime("%b %d %Y")


@dataclass
class MonthDate:
    date: datetime
    
    @property
    def fr(self):
        return self.date.strftime("%Y-%m")
    @property
    def en(self):
        return self.date.strftime("%Y-%m")


@dataclass
class Event:
    date: Date
    description: String


@dataclass
class Symptom:
    name: String
    start_date: String
    #triggers: String
    current_status: String
    notes: String
    
    @property
    def subtotal_dollar(self):
        return f'${self.subtotal:.2f}'

