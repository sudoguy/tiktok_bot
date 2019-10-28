from typing import List

from pydantic import BaseModel
from typing_extensions import Literal

from .category import ChallengeInfo
from .request import CountOffsetParams, ListRequestParams, ListResponseData
from .user import CommonUserDetails


class SearchRequest(ListRequestParams, CountOffsetParams):
    # The term to search for
    keyword: str


class UserSearchRequest(SearchRequest):
    # Required - the scope of the search - users = 1.
    type: int = 1


class SubstringPosition(BaseModel):
    """
    Represents the location of a substring in a string.
    e.g. For the string "The quick brown fox", the substring "quick" would be:
    {
        begin: 4,
        end: 8
    }
    """

    # The start index of the substring
    begin: int

    # The end index of the substring
    end: int


class UserSearchResult(BaseModel):
    # If the user's nickname contains the search term, this array contains the location of the term
    position: List[SubstringPosition] = None

    # If the user's username (unique_id) contains the search term,
    # this array contains the location of the term
    uniqid_position: List[SubstringPosition] = None

    # Information about the user
    user_info: CommonUserDetails


class UserSearchResponse(ListResponseData, CountOffsetParams):
    # A list of users that match the search term
    user_list: List[UserSearchResult]

    # The scope of the search - users = 1
    type: int


class HashtagSearchResult(BaseModel):
    # Information about the hashtag
    challenge_info: ChallengeInfo

    # If the hashtag contains the search term, this array contains the location of the term
    position: List[SubstringPosition] = None


class HashtagSearchResponse(ListResponseData, CountOffsetParams):
    # A list of hashtags that match the search term
    challenge_list: List[HashtagSearchResult]

    # True if a challenge matches the search term
    is_match: bool

    # 1 if the search term is disabled
    keyword_disabled: Literal[0, 1]
