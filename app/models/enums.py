from enum import Enum


class TicketStatus(Enum):
    """
    Class for enum representing status of tickets
    """
    PENDING = "pending"
    IN_REVIEW = "in review"
    CLOSED = "closed"
