from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Recommendation(str, Enum):
    APPROVE = "APPROVE"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    REJECT = "REJECT"


class RiskAssessment(BaseModel):
    riskLevel: RiskLevel
    fraudScore: int = Field(ge=0, le=100)
    recommendation: Recommendation


class FraudAnalysisResult(BaseModel):
    summary: str
    riskAssessment: RiskAssessment
    observations: List[str] = Field(default_factory=list)
    potentialIssues: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
