from typing import List

from pydantic import BaseModel
from typing_extensions import Literal

from .request import (
    BaseResponseData,
    ListRequestParams,
    ListResponseData,
    TimeOffsetRequestParams,
    TimeOffsetResponseParams,
)
from .user import CommonUserDetails


class FollowRequest(BaseResponseData):
    # The id of the user to follow
    user_id: str

    # 0 to unfollow, 1 to follow
    type: Literal[0, 1]


class FollowResponse(BaseResponseData):
    # 0 if not following, 1 if following
    follow_status: Literal[0, 1]

    # 0 if not watching, 1 if watching
    watch_status: Literal[0, 1]


class ListReceivedFollowRequestsRequest(ListRequestParams, TimeOffsetRequestParams):
    pass


class ListReceivedFollowRequestsResponse(ListResponseData, TimeOffsetResponseParams):
    # A list of users who have requested to follow you
    request_users: List[CommonUserDetails]


class ApproveFollowRequest(BaseModel):
    # The id of the user to approve
    from_user_id: str


class ApproveFollowResponse(BaseResponseData):
    # 0 if the user was successfully approved
    approve_status: int


class RejectFollowRequest(BaseModel):
    # The id of the user to reject
    from_user_id: str


class RejectFollowResponse(BaseResponseData):
    # 0 if the user was successfully rejected
    reject_status: int
