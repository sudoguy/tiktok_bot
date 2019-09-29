from tiktok_bot.client import HTTPClient
from tiktok_bot.models.category import ListCategoriesRequest, ListCategoriesResponse
from tiktok_bot.models.feed import ListFeedRequest, ListFeedResponse, ListForYouFeedResponse
from tiktok_bot.models.login import LoginRequest, LoginResponse
from tiktok_bot.models.search import (
    HashtagSearchResponse,
    SearchRequest,
    UserSearchRequest,
    UserSearchResponse,
)
from tiktok_bot.models.user import UserProfileResponse

from .config import DEFAULT_HEADERS, DEFAULT_PARAMS


class TikTokAPI:
    def __init__(self):
        self.client = HTTPClient(
            base_url="https://api2.musical.ly/",
            default_headers=DEFAULT_HEADERS,
            default_params=DEFAULT_PARAMS,
        )

    @staticmethod
    def encrypt_with_XOR(value: str, key=5) -> str:
        return "".join([hex(int(x ^ key))[2:] for x in value.encode("utf-8")])

    def login(self, login_request: LoginRequest) -> LoginResponse:
        """ FIXME: Under development """

        url = "passport/user/login/"

        response = self.client.post(url=url, data=login_request.dict())

        login = LoginResponse(**response.json())

        return login

    def login_with_email(self, email: str, password: str):
        """ FIXME: Under development """

        email = self.encrypt_with_XOR(email)
        password = self.encrypt_with_XOR(password)

        request = LoginRequest(email=email, password=password)

        return self.login(request)

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

    def get_user(self, user_id: str) -> UserProfileResponse:
        "Gets a user's profile."

        url = "aweme/v1/user/"

        response = self.client.get(url=url, params={"user_id": user_id})

        user = UserProfileResponse(**response.json())

        return user

    def search_users(self, user_search_request: UserSearchRequest) -> UserSearchResponse:
        "Searches for users."

        url = "aweme/v1/discover/search/"

        response = self.client.get(url=url, params=user_search_request.dict())

        user_search = UserSearchResponse(**response.json())

        return user_search

    def search_hashtags(self, hashtag_search_request: SearchRequest) -> HashtagSearchResponse:
        "Searches for hashtags."

        url = "aweme/v1/challenge/search/"

        response = self.client.get(url=url, params=hashtag_search_request.dict())

        hashtag_search = HashtagSearchResponse(**response.json())

        return hashtag_search
