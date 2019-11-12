<p align="center"><strong>TikTok-Bot</strong> <em>- Free and smart bot for Python.</em></p>

<p align="center">
<a href="https://travis-ci.org/sudoguy/tiktok_bot">
    <img src="https://travis-ci.org/sudoguy/tiktok_bot.svg?branch=master" alt="Build Status">
</a>
<a href="https://pepy.tech/project/tiktok-bot">
    <img src="https://pepy.tech/badge/tiktok-bot" alt="Downloads">
</a>
<a href="https://pypi.org/project/httpx/">
    <img src="https://badge.fury.io/py/httpx.svg" alt="Package version">
</a>
</p>


**Note**: *This project should be considered as an **"alpha"** release.*

---

## Quickstart

```python
from tiktok_bot import TikTokBot

bot = TikTokBot()

# getting your feed (list of posts)
my_feed = bot.list_for_you_feed(count=25)

popular_posts = [for post in my_feed if post.statistics.play_count > 1_000_000]

# extract video urls without watermark (every post has helpers)
urls = [post.video_url_without_watermark for post in popular_posts]
```

## Installation

Install with pip:

```shell
pip install tiktok-bot
```
tiktok-bot requires Python 3.6+
