import pytest

from tiktok_bot.api import TikTokAPI


@pytest.fixture()
def api():
    return TikTokAPI()
