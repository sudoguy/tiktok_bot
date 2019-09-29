from tiktok_bot.api import TikTokAPI


def test_encrypt_with_xor(api: TikTokAPI):
    assert api.encrypt_with_XOR("user@example.com") == "7076607745607d64687569602b666a68"
    assert api.encrypt_with_XOR("password") == "75647676726a7761"
