from typing import List

from .post import Post
from .request import CountOffsetParams, ListRequestParams, ListResponseData


class ListPostsInHashtagRequest(ListRequestParams, CountOffsetParams):
    # The ID of the hashtag
    ch_id: str

    # ??? - set to 0
    query_type: int

    # ??? - set to 5
    type: int


class ListPostsInHashtagResponse(ListResponseData, CountOffsetParams):
    # A list of posts containing the hashtag
    aweme_list: List[Post]
