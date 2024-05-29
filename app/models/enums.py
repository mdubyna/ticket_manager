from enum import Enum


class TicketStatus(Enum):
    PENDING = "pending"
    IN_REVIEW = "in review"
    CLOSED = "closed"
