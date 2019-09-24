from tiktok_bot.client import HTTPClient
from tiktok_bot.models.category import ListCategoriesRequest, ListCategoriesResponse
from tiktok_bot.models.feed import ListFeedRequest, ListFeedResponse, ListForYouFeedResponse

from .config import DEFAULT_HEADERS, DEFAULT_PARAMS


class TikTokAPI:
    def __init__(self):
        self.client = HTTPClient(
            base_url="https://api2.musical.ly/",
            host="api2.musical.ly",
            default_headers=DEFAULT_HEADERS,
            default_params=DEFAULT_PARAMS,
        )

    def list_for_you_feed(self, list_feed_request: ListFeedRequest) -> ListForYouFeedResponse:
        "Lists posts in the For You feed."

        url = "aweme/v1/feed/"

        response = self.client.get(url=url, params=list_feed_request.dict())

        feed = ListForYouFeedResponse(**response.json())

        return feed

    def list_following_feed(self, list_feed_request: ListFeedRequest) -> ListFeedResponse:
        "Lists posts in the Following feed."

        url = "aweme/v1/feed/"

        response = self.client.get(url=url, params=list_feed_request.dict())

        feed = ListFeedResponse(**response.json())

        return feed

    def list_categories(
        self, list_categories_request: ListCategoriesRequest
    ) -> ListCategoriesResponse:
        "Lists popular categories/hashtags."

        url = "aweme/v1/category/list/"

        response = self.client.get(url=url, params=list_categories_request.dict())

        categories = ListCategoriesResponse(**response.json())

        return categories
