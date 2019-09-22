from enum import IntEnum


class FeedType(IntEnum):
    ForYou = 0
    Following = 1


class PullType(IntEnum):
    # The feed was loaded by default, e.g. by clicking the tab or loading the app
    Default = 0

    # The feed was explicitly refreshed by the user, e.g. by swiping down
    Refresh = 1

    # More posts were requested by the user, e.g. by swiping up
    LoadMore = 2
