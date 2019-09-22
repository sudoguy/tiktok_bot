"""
  Represents a text link to a user, e.g. "@username" in a comment
"""
from pydantic import BaseModel


class Tag(BaseModel):
    # The type of user being tagged?
    at_user_type: str

    # The zero-based index in the text where the tag starts
    end: int

    # The zero-based index in the text where the tag ends
    start: int

    # The type of tag?
    type: int

    # The ID of the user being tagged
    user_id: str
