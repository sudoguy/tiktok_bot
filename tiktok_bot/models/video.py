from pydantic import BaseModel

from .request import Media


class Video(BaseModel):
    # A medium version of the video's cover image
    cover: Media

    # A high-quality link to download the video
    download_addr: Media

    # The video's duration in milliseconds
    duration: int

    # Whether the download link has a watermark
    has_watermark: bool

    # The video's height, e.g. 960
    height: int

    # A high-quality version of the video's cover image
    origin_cover: Media

    # The quality of the video, e.g. 720p
    ratio: str

    # The video's width, e.g. 540
    width: int
