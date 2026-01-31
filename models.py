from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime


class Message(BaseModel):
    sender: str
    text: Optional[str] = ""
    timestamp: Optional[str] = None

    def normalize(self):
        return {
            "sender": self.sender,
            "text": self.text or "",
            "timestamp": self.timestamp or datetime.utcnow().isoformat()
        }


class RequestModel(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: Optional[List[Message]] = []
    metadata: Optional[Dict] = {}


class EngagementMetrics(BaseModel):
    engagementDurationSeconds: int
    totalMessagesExchanged: int


class Intelligence(BaseModel):
    bankAccounts: List[str]
    upiIds: List[str]
    phishingLinks: List[str]


class AgentExplanation(BaseModel):
    confidence: str
    scamCategory: str
    detectionSignals: List[str]
    recommendedAction: str
    systemRationale: str


class ResponseModel(BaseModel):
    status: str
    scamDetected: bool
    engagementMetrics: EngagementMetrics
    extractedIntelligence: Intelligence
    agentNotes: str
    agentExplanation: AgentExplanation