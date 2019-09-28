from typing import List, Union

from pydantic import BaseModel


class LoginRequest(BaseModel):
    # Unsure, but looks to be hard-coded to 1
    mix_mode: int = 1

    # The unique username ("musername") of the user
    username: str = ""

    # The email address associated with the user account
    email: str = ""

    # The mobile number associated with the user account
    mobile: str = ""

    # ???
    account: str = ""

    # The password to the user account
    password: str = ""

    # The captcha answer - only required if a captcha was shown
    captcha: str = ""


class LoginSuccessData(BaseModel):
    # ???
    area: str

    # The URL of the user's avatar
    avatar_url: str

    # ???
    bg_img_url: str

    # The user's birthday
    birthday: str

    # If the user allows people to find them by their phone number
    can_be_found_by_phone: int

    # ???
    connects: List[BaseModel]

    # ???
    description: str

    # The email address associated with the account
    email: str

    # The number of users that follow the user
    followers_count: int

    # The number of users the user is following
    followings_count: int

    # An integer representing the gender of the user
    gender: int

    # ???
    industry: str

    # Indicates if the user account is blocked
    is_blocked: int

    # ???
    is_blocking: int

    # ???
    is_recommend_allowed: int

    # ???
    media_id: int

    # The mobile number of the user
    mobile: str

    # The name of the user - does not appear to be used
    name: str

    # Indicates if the user is new or not
    new_user: int

    # A Chinese character hint
    recommend_hint_message: str

    # The screen name of the user - does not appear to be used
    screen_name: str

    # The session ID used to authenticate subsequent requests in the sessionid cookie
    session_key: str

    # ???
    skip_edit_profile: int

    # ???
    user_auth_info: str

    # The ID of the user
    user_id: str

    # If the user is verified or not
    user_verified: bool

    # ???
    verified_agency: str

    # ???
    verified_content: str

    # The number of users that have visited the user's profile recently
    visit_count_recent: int


class LoginErrorData(BaseModel):
    # If required, the captcha that must solved
    captcha: str

    # A message explaining why the request failed
    description: str

    # An error code
    error_code: int


class LoginResponse(BaseModel):
    data: Union[LoginSuccessData, LoginErrorData]

    # A message indicating whether the request was successful or not
    message: str
