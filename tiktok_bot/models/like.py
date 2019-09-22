from typing_extensions import Literal

from .request import BaseResponseData


class LikePostRequest(BaseResponseData):
    # The id of the post to like
    aweme_id: str

    # 0 to unlike, 1 to like
    type: Literal[0, 1]


class LikePostResponse(BaseResponseData):
    #
    # 0 if liked, 1 if not liked
    #
    # Note: for some reason, this value is the opposite of what you would expect
    is_digg: Literal[0, 1]
