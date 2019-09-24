from typing import List

from pydantic import BaseModel

from .music import MusicTrack
from .request import (
    BaseResponseData,
    CursorOffsetRequestParams,
    CursorOffsetResponseParams,
    ListRequestParams,
    ListResponseData,
)
from .user import CommonUserDetails
from .video import Video


class PostStatistics(BaseModel):
    # The ID of the post
    aweme_id: str

    # The number of comments on the post
    comment_count: int

    # The number of times the post has been liked
    digg_count: int

    # The number of times the post has been forwarded (looks unused?)
    forward_count: int = None

    # The number of times the post has been viewed - doesn't appear to be public, so always 0
    play_count: int

    # The number of times the post has been shared
    share_count: int


class PostStatus(BaseModel):
    # True if the post allows comments
    allow_comment: bool

    # True if the post allows sharing
    allow_share: bool

    # 0 if the post can be downloaded
    download_status: int

    # True if the post is currently being reviewed
    in_reviewing: bool = None

    # True if the post has been deleted
    is_delete: bool

    # True if the post is private
    is_private: bool

    # True if the post contains content that is not allowed on the platform
    is_prohibited: bool = None

    # 0 if the post is public
    private_status: int = None

    # 1 if the post has been reviewed
    reviewed: int = None


class PostTags(BaseModel):
    # 0 if the tag is for a user; 1 if the tag is for a hashtag
    type: int

    # The name of the hashtag
    hashtag_name: str = None

    # The ID of the tagged user
    user_id: str = None


class RiskInfo(BaseModel):
    # The text shown if the post has been flagged
    content: str

    # ???
    risk_sink: bool = False

    # The risk type associated with the post - 0 if no risk; 1 if low; 2 if high
    type: int

    # ??? - only present if the post has been flagged
    vote: bool = None

    # True if a warning should be shown to the user
    warn: bool


class ShareInfo(BaseModel):
    # ???
    bool_persist: int = None

    # The description used when sharing (if set)
    share_desc: str

    # The description used when sharing a link only (if set)
    share_link_desc: str = None

    # The quote used when sharing (if set)
    share_quote: str = None

    # The signature used when sharing (if set)
    share_signature_desc: str = None

    # The signature URL used when sharing (if set)
    share_signature_url: str = None

    # The title used when sharing
    share_title: str

    # The link to share
    share_url: str

    # The description used when sharing on Weibo
    share_weibo_desc: str


class StickerInfo(BaseModel):
    # The ID of the sticker, e.g. 22094
    id: str

    # The display name of the sticker, e.g. Long Face
    name: str


class Post(BaseModel):
    # Details about the author
    author: CommonUserDetails = None

    # The ID of the author
    author_user_id: str

    # The ID of the post
    aweme_id: str

    # The type of post - 0 for a musical.ly
    aweme_type: int

    # The timestamp in seconds when the post was created
    create_time: int

    # A description of the post
    desc: str

    # Details about the music used in the post
    music: MusicTrack = None

    # True if the end user should not be provided the option to download the video
    prevent_download: bool = None

    # An age rating for the post, e.g. 12
    rate: int

    # The 2-letter region the post was created in, e.g. US
    region: str

    # Risk information about the post
    risk_infos: RiskInfo = None

    # Information used when sharing the post
    share_info: ShareInfo = None

    # A link to the video on the musical.ly website that is used when sharing
    share_url: str

    # Statistics about the post
    statistics: PostStatistics

    # Status information about the post
    status: PostStatus

    # Information about the sticker used in the post
    sticker_detail: StickerInfo = None

    # The ID of the sticker used in the post (looks to be deprecated by sticker_detail)
    stickers: str = None

    # Tagged users and hashtags used in the description
    text_extra: List[PostTags]

    # 1 if the logged in user has liked this post
    user_digged: int

    # Details about the video in the post
    video: Video


class GetPostResponse(BaseResponseData):
    aweme_detail: Post


class ListPostsRequest(ListRequestParams, CursorOffsetRequestParams):
    # The id of the user whose posts to retrieve
    user_id: str


class ListPostsResponse(ListResponseData, CursorOffsetResponseParams):
    aweme_list: List[Post]
