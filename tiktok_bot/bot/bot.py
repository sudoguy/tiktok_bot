from typing import List

from tiktok_bot.api import TikTokAPI
from tiktok_bot.models.category import Category, ListCategoriesRequest
from tiktok_bot.models.feed import ListFeedRequest
from tiktok_bot.models.feed_enums import FeedType, PullType
from tiktok_bot.models.post import Post


class TikTokBot:
    def __init__(self):
        self.api = TikTokAPI()

    def list_categories(self, count: int = 10, cursor: int = 0) -> List[Category]:
        request = ListCategoriesRequest(count=count, cursor=cursor)
        categories = self.api.list_categories(request)

        return categories.category_list

    def list_for_you_feed(self, count: int = 6, cursor: int = 0) -> List[Post]:
        request = ListFeedRequest(
            count=count,
            max_cursor=cursor,
            pull_type=PullType.LoadMore,
            type=FeedType.ForYou,
            is_cold_start=1,
        )
        feed = self.api.list_for_you_feed(request)

        return feed.aweme_list

    def list_following_feed(self, count: int = 6, cursor: int = 0) -> List[Post]:
        """
        Lists posts in the Following feed.

        * Login required
        """
        request = ListFeedRequest(
            count=count,
            max_cursor=cursor,
            pull_type=PullType.LoadMore,
            type=FeedType.Following,
            is_cold_start=1,
        )
        feed = self.api.list_following_feed(request)

        return feed.aweme_list
