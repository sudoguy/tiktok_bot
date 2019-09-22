from typing import List

from .request import (
    ListRequestParams,
    ListResponseData,
    TimeOffsetRequestParams,
    TimeOffsetResponseParams,
)
from .user import CommonUserDetails


class ListFollowersRequest(ListRequestParams, TimeOffsetRequestParams):
    # The id of the user whose followers to retrieve
    user_id: str


class ListFollowersResponse(ListResponseData, TimeOffsetResponseParams):
    # A list of the user's followers
    followers: List[CommonUserDetails]


class ListFollowingRequest(ListRequestParams, TimeOffsetRequestParams):
    # The id of the user whose followers to retrieve
    user_id: str


class ListFollowingResponse(ListResponseData, TimeOffsetResponseParams):
    # A list of users the user is following
    followings: List[CommonUserDetails]
