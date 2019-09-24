from typing import List, Union

from pydantic import BaseModel, Schema

from .post import Post
from .request import CountOffsetParams, ListRequestParams, ListResponseData
from .user import CommonUserDetails


class ChallengeInfo(BaseModel):
    # The user who created the challenge, or an empty object
    author: Union[CommonUserDetails, BaseModel]

    # The name of the challenge
    cha_name: str

    # The ID of the challenge
    cid: str

    # A description of the challenge
    desc: str

    # ???
    is_pgcshow: bool

    # An in-app link to the challenge
    schema_: str = Schema(default=..., alias="schema")

    # The type of challenge - 0 for hashtag?
    type: int

    # The number of users who have uploaded a video for the challenge
    user_count: int

    class Config:
        fields = {"schema_": "schema"}


class Category(BaseModel):
    # A list of posts in the category
    aweme_list: List[Post]

    # The type of category - 0 for hashtag?
    category_type: int

    # Information about the category
    challenge_info: ChallengeInfo

    # A description of the category type, e.g. "Trending Hashtag"
    desc: str


class ListCategoriesRequest(ListRequestParams, CountOffsetParams):
    pass


class ListCategoriesResponse(ListResponseData, CountOffsetParams):
    # A list of categories
    category_list: List[Category]
