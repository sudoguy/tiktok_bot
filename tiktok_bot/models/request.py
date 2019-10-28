import abc
from typing import List, Optional, Union

from pydantic import BaseModel


class RequiredUserDefinedRequestParams(BaseModel, abc.ABC):
    # The 16-character ID of your installation, e.g. 4549764744226841084
    iid: str

    # A 16-character hexadecimal identifier associated with your device, e.g. 4b903fbb9d457937
    openudid: str

    # The ID of your device that has already been registered with musical.ly
    device_id: str

    # An anti-fraud fingerprint of your device requested from a different API
    fp: str


class StaticRequestParams(RequiredUserDefinedRequestParams):
    # Your Android version, e.g. 23
    os_api: str

    # Your device model, e.g. Pixel 2
    device_type: str

    # ??? - set to "a"
    ssmix: str

    # The SS_VERSION_CODE metadata value from the AndroidManifest.xml file, e.g. 2018060103
    manifest_version_code: str

    # Your device's pixel density, e.g. 480
    dpi: int

    # The application name - hard-coded to "musical_ly"
    app_name: str

    # The SS_VERSION_NAME metadata value from the AndroidManifest.xml file, e.g. 7.2.0
    version_name: str

    # The UTC offset in seconds of your timezone, e.g. 37800 for Australia/Lord_Howe
    timezone_offset: int

    # ??? - are we in China / using the Chinese version? Set to 0
    is_my_cn: int

    # Network connection type, e.g. "wifi"
    ac: str

    # The UPDATE_VERSION_CODE metadata value from the AndroidManifest.xml file, e.g. 2018060103
    update_version_code: str

    # The channel you downloaded the app through, e.g. googleplay
    channel: str

    # Your device's platform, e.g. android
    device_platform: str

    # The build int of the application, e.g. 7.2.0
    build_number: str

    # A numeric version of the version_name metadata value, e.g. 720
    version_code: int

    # The name of your timezone as per the tz database, e.g. Australia/Sydney
    timezone_name: str

    # The region of the account you are logging into, e.g. AU.
    # This field is only present if you are logging in from a device that hasn't had a
    # user logged in before.
    account_region: Optional[str] = None

    # Your Optional[str]ice's resolution, e.g. 1080*1920
    resolution: str

    # Your device's operating system version, e.g. 8.0.0
    os_version: str

    # Your device's brand, e.g. Google
    device_brand: str

    # ??? - empty
    mcc_mnc: str

    # The application's two-letter language code, e.g. en
    app_language: str

    # Your i18n language, e.g. en
    language: str

    # Your region's i18n locale, e.g. US
    region: str

    # Your device's i18n locale, e.g. US
    sys_region: str

    # Your carrier's region (a two-letter country code), e.g. AU
    carrier_region: str

    # You carrer's mobile country code (MCC), e.g. 505
    carrier_region_v2: str

    # A hard-coded i18n constant set to "1233"
    aid: str

    # ??? - set to 1
    pass_region: int

    # ??? - set to 1
    pass_route: int

    class Config:
        fields = {"pass_region": "pass-region", "pass_route": "pass-route"}


class AntiSpamParams(BaseModel):
    # A 20-character anti-spam parameter
    as_: str

    # A 20-character anti-spam parameter
    cp: str

    # An encoded version of the 'as' anti-spam parameter
    mas: str

    class Config:
        fields = {"as_": "as"}


class BaseRequestParams(StaticRequestParams, AntiSpamParams):
    # The current timestamp in seconds since UNIX epoch
    ts: int

    # The current timestamp in milliseconds since UNIX epoch
    _rticket: str


class ListRequestParams(BaseModel):
    # The number of results to return
    count: int = 10

    # How the request will be retried on failure - defaults to "no_retry"
    retry_type: Optional[str] = None


class TimeOffsetRequestParams(BaseModel):
    """
    A timestamp in seconds - the most recent results before this time will be listed.
    Use min_time from the response data here for pagination.
    """

    max_time: int


class TimeOffsetResponseParams(BaseModel):
    # The timestamp in seconds associated with the first result
    max_time: int

    # The timestamp in seconds associated with the last result - use as max_time for pagination
    min_time: int


class CursorOffsetRequestParams(BaseModel):
    """
    A timestamp in milliseconds - the most recent results before this time will be listed.
    Use max_cursor from the response data here for pagination. Use 0 for the most recent.
    """

    max_cursor: int


class CursorOffsetResponseParams(BaseModel):
    # The timestamp in milliseconds associated with the first result
    min_cursor: int

    # The timestamp in milliseconds associated with the last result - use for pagination
    max_cursor: int


class CountOffsetParams(BaseModel):
    # The number of results to skip
    cursor: int = 0


class ExtraResponseData(BaseModel):
    # ???
    fatal_item_ids: List[int] = None

    # A log ID for this request
    logid: Optional[str] = None

    # The current timestamp in milliseconds
    now: int


class BaseResponseData(BaseModel, abc.ABC):
    # 0 if the request was successful
    status_code: int

    extra: ExtraResponseData


class ListResponseData(BaseResponseData):
    # Whether there are more results that can be requested
    has_more: Union[bool, int]

    # The total number of results returned - not present in all list requests
    total: Optional[int] = None


class Media(BaseModel):
    # A list of HTTP URLs to this media
    url_list: List[str]
