import sys
from typing import List

from loguru import logger
from typing_extensions import Literal

from tiktok_bot.api import TikTokAPI
from tiktok_bot.models.category import Category, ListCategoriesRequest
from tiktok_bot.models.feed import ListFeedRequest
from tiktok_bot.models.feed_enums import FeedType, PullType
from tiktok_bot.models.post import Post
from tiktok_bot.models.user import CommonUserDetails, UserProfile


class TikTokBot:
    def __init__(self, log_level: Literal["INFO", "DEBUG"] = "INFO"):
        self.api = TikTokAPI()

        logger.remove()
        logger.add(sys.stderr, level=log_level)

    def list_categories(self, count: int = 10, cursor: int = 0) -> List[Category]:
        request = ListCategoriesRequest(count=count, cursor=cursor)
        categories = self.api.list_categories(request)

        return categories.category_list

    def get_user_by_id(self, user_id: str) -> UserProfile:
        user_response = self.api.get_user(user_id)

        return user_response.user

    def search_users(self, keyword: str, count: int = 6) -> List[CommonUserDetails]:
        users_search = self.api.search_users(keyword=keyword, count=count)

        users = [user.user_info for user in users_search]

        return users

    def list_for_you_feed(self, count: int = 6) -> List[Post]:
        feed = self.api.list_for_you_feed(count)

        return feed

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
