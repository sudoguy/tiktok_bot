from typing import List

from pydantic import BaseModel
from typing_extensions import Literal

from .request import BaseResponseData, CountOffsetParams, ListRequestParams, ListResponseData
from .tag import Tag
from .user import CommonUserDetails


class Comment(BaseModel):
    # The ID of the post
    aweme_id: str

    # The ID of the comment
    cid: str

    # The timestamp in seconds when the comment was posted
    create_time: int

    # The number of times the comment has been liked
    digg_count: int

    # If this comment is replying to a comment, this array contains the original comment
    reply_comment: List["Comment"] = None

    # If this comment is replying to a comment, the ID of that comment - "0" if not a reply
    reply_id: str

    # The status of the comment - 1 = published, 4 = published by you?
    status: int

    # The comment text
    text: str

    # Details about any tags in the comment
    text_extra: List[Tag]

    # Details about the author
    user: CommonUserDetails

    # 1 if the user likes the comment
    user_digged: Literal[0, 1]


class ListCommentsRequest(ListRequestParams, CountOffsetParams):
    # The ID of the post to list comments for
    aweme_id: str

    # ??? - default is 2
    comment_style: int = None

    # ???
    digged_cid = None

    # ???
    insert_cids = None


class ListCommentsResponse(ListResponseData, CountOffsetParams):
    comments: List[Comment]


class PostCommentRequest(BaseModel):
    # The ID of the post to comment on
    aweme_id: str

    # The comment text
    text: str

    # The ID of the comment that is being replied to
    reply_id: str = None

    # Details about any tags in the comment
    text_extra: List[Tag]

    # ???
    is_self_see: Literal[0, 1]


class PostCommentResponse(BaseResponseData):
    # The comment that was posted
    comment: Comment
