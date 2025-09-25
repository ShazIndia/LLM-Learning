from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class ProblemCategory(str, Enum):
    TECHNICAL = "technical"
    SOFTWARE = "software"
    HARDWARE = "hardware"
    NETWORK = "network"
    GENERAL = "general"

class TroubleshootRequest(BaseModel):
    problem_description: str = Field(
        ..., 
        min_length=10, 
        max_length=2000,
        description="Detailed description of the problem"
    )
    category: ProblemCategory = Field(
        default=ProblemCategory.GENERAL,
        description="Category of the problem"
    )
    urgency: Optional[str] = Field(
        default="medium",
        regex="^(low|medium|high|critical)$",
        description="Urgency level of the problem"
    )
    additional_context: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Any additional context or details"
    )

class Solution(BaseModel):
    step: int
    description: str
    estimated_time: Optional[str] = None

class TroubleshootResponse(BaseModel):
    problem_summary: str
    solutions: List[Solution]
    confidence_score: float = Field(ge=0.0, le=1.0)
    additional_resources: Optional[List[str]] = None
    estimated_total_time: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    message: str
