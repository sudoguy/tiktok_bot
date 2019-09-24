from tiktok_bot.api import TikTokAPI
from tiktok_bot.models.category import ListCategoriesRequest


class TikTokBot:
    def __init__(self):
        self.api = TikTokAPI()

    def list_categories(self, count: int = 10, cursor: int = 0):
        request = ListCategoriesRequest(count=count, cursor=cursor)
        categories = self.api.list_categories(request)

        return categories
