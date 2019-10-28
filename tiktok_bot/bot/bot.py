from typing import List

from tiktok_bot.api import TikTokAPI
from tiktok_bot.models.category import Category, ListCategoriesRequest
from tiktok_bot.models.feed import ListFeedRequest
from tiktok_bot.models.feed_enums import FeedType, PullType
from tiktok_bot.models.post import Post
from tiktok_bot.models.search import UserSearchRequest
from tiktok_bot.models.user import CommonUserDetails, UserProfile


class TikTokBot:
    def __init__(self):
        self.api = TikTokAPI()

    def list_categories(self, count: int = 10, cursor: int = 0) -> List[Category]:
        request = ListCategoriesRequest(count=count, cursor=cursor)
        categories = self.api.list_categories(request)

        return categories.category_list

    def get_user_by_id(self, user_id: str) -> UserProfile:
        user_response = self.api.get_user(user_id)

        return user_response.user

    def search_user(
        self, keyword: str, count: int = 10, cursor: int = 0
    ) -> List[CommonUserDetails]:
        request = UserSearchRequest(keyword=keyword, count=count, cursor=cursor)

        user_search = self.api.search_users(request)

        users = [user.user_info for user in user_search.user_list]

        return users

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
