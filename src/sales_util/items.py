from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str 
    peakCCU: int 
    required_age: int 
    price: float 
    dlcCount: int 
    supportWindows: bool 
    supportMac: bool 
    supportLinux: bool 
    positive: int 
    negative: int 
    achievements: int 
    recommendations: Optional[int] = None 
    release_year: Optional[int] = None 
    release_month: Optional[int] = None 
    release_day: Optional[int] = None 
    small_description: Optional[str] = None 
    estimatedOwners: Optional[int] = None 
    supported_languages: Optional[int] = None 
    num_developers: Optional[int] = None 
    num_publishers: Optional[int] = None 
    num_categories: Optional[int] = None 
    num_genres: Optional[int] = None