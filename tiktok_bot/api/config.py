# ToDo: Make it configurable
DEFAULT_PARAMS = {
    "os_api": "23",
    "device_type": "Pixel",
    "ssmix": "a",
    "manifest_version_code": "2018111632",
    "dpi": 420,
    "app_name": "musical_ly",
    "version_name": "9.1.0",
    "timezone_offset": 36000,
    "is_my_cn": 0,
    "ac": "wifi",
    "update_version_code": "2018111632",
    "channel": "googleplay",
    "device_platform": "android",
    "build_number": "9.1.0",
    "version_code": 910,
    "timezone_name": "Australia/Brisbane",
    "resolution": "1080*1920",
    "os_version": "7.1.2",
    "device_brand": "Google",
    "mcc_mnc": "",
    "app_language": "en",
    "language": "en",
    "region": "US",
    "sys_region": "US",
    "carrier_region": "AU",
    "carrier_region_v2": "505",
    "aid": "1233",
    "pass-region": 1,
    "pass-route": 1,
}
# ToDo: Fix this
DEFAULT_HEADERS = {
    "Host": "api2.musical.ly",
    "X-SS-TC": "0",
    "User-Agent": f"com.zhiliaoapp.musically/{DEFAULT_PARAMS['manifest_version_code']}"
    + f" (Linux; U; Android {DEFAULT_PARAMS['os_version']};"
    + f" {DEFAULT_PARAMS['language']}_{DEFAULT_PARAMS['region']};"
    + f" {DEFAULT_PARAMS['device_type']};"
    + f" Build/NHG47Q; Cronet/58.0.2991.0)",
    "Accept-Encoding": "gzip",
    "Connection": "keep-alive",
    "X-Tt-Token": "",
    "sdk-version": "1",
}
