from typing import Any, List

from pydantic import BaseModel

from .post import Post
from .request import BaseResponseData, CountOffsetParams, ListRequestParams, ListResponseData, Media


class Sticker(BaseModel):
    # ???
    children: Any

    # A description of the sticker
    desc: str

    # The ID of the sticker
    effect_id: str

    # The icon associated with the sticker
    icon_url: Media

    # The ID of the sticker
    id: str

    # True if the current user has favorited the sticker
    is_favorite: bool

    # The name of the sticker
    name: str

    # The ID the user that owns the sticker (empty if owned by the Effect Assistant)
    owner_id: str

    # The nickname of the owner, e.g. "Effect Assistant"
    owner_nickname: str

    # ???
    tags: List[Any]

    # The total number of posts using this sticker
    user_count: int


class ListPostsByStickerRequest(ListRequestParams, CountOffsetParams):
    # The ID of the sticker
    sticker_id: str


class ListPostsByStickerResponse(ListResponseData, CountOffsetParams):
    # A list of posts using the sticker
    aweme_list: List[Post]

    # Currently empty
    stickers: List[Any]


class GetStickersRequest(BaseModel):
    # A list of sticker ids to get information about
    sticker_ids: str


class GetStickersResponse(BaseResponseData):
    sticker_infos: List[Sticker]
