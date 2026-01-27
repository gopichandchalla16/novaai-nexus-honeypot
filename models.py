from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    sender: str
    text: str
    timestamp: str

class RequestModel(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message] = []
    metadata: Optional[dict] = {}

class EngagementMetrics(BaseModel):
    engagementDurationSeconds: int
    totalMessagesExchanged: int

class Intelligence(BaseModel):
    bankAccounts: List[str]
    upiIds: List[str]
    phishingLinks: List[str]

class ResponseModel(BaseModel):
    status: str
    scamDetected: bool
    engagementMetrics: EngagementMetrics
    extractedIntelligence: Intelligence
    agentNotes: str