from typing import Union

from pydantic import BaseModel

from .request import BaseResponseData, Media


class CommonUserDetails(BaseModel):
    # A large version of the user's avatar
    avatar_larger: Media

    # A medium version of the user's avatar
    avatar_medium: Media

    # A thumbnail version of the user's avatar
    avatar_thumb: Media

    # The timestamp in seconds when the user's account was created
    create_time: int = None

    # The badge name with a verified user (e.g. comedian, style guru)
    custom_verify: str

    # 1 if you follow this user
    follow_status: int

    # 1 if this user follows you
    follower_status: int

    # The user's Instagram handle
    ins_id: str

    # Indicates if the user has been crowned
    is_verified: bool

    # The user's profile name
    nickname: str

    # A 2-letter country code representing the user's region, e.g. US
    region: str

    # If the user is live, a str ID used to join their stream, else 0
    room_id: Union[str, int] = None

    # 1 if the user's profile is set to private
    secret: int

    # The user's profile signature
    signature: str

    # The user's Twitter handle
    twitter_id: str

    # The user's ID
    uid: str

    # The user's musername
    unique_id: str

    # 1 if the user has been crowned
    verification_type: int

    # The user's YouTube channel ID
    youtube_channel_id: str


class UserProfile(CommonUserDetails):
    # The number of videos the user has uploaded
    aweme_count: int

    # The number of videos the user has liked
    favoriting_count: int

    # The number of users who follow this user
    follower_count: int

    # The number of users this user follows
    following_count: int

    # The total number of likes the user has received
    total_favorited: int


class UserProfileResponse(BaseResponseData):
    user: UserProfile
