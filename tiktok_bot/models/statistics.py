from pydantic import BaseModel


class Statistics(BaseModel):
    aweme_id: str
    comment_count: int
    digg_count: int
    download_count: int
    forward_count: int
    lose_comment_count: int
    lose_count: int
    play_count: int
    share_count: int
