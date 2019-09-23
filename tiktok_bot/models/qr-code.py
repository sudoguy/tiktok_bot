from typing import List

from pydantic import BaseModel

from .request import BaseResponseData


class QRCodeRequest(BaseModel):
    # The internal version to use; currently 4
    schema_type: int

    # The ID of the user to get a QR code for
    object_id: str


class QRCodeUrl(BaseModel):
    # An in-app link to the QR code
    uri: str

    # Contains a public link to the QR code image (first element in array)
    url_list: List[str]


class QRCodeResponse(BaseResponseData):
    # Contains a link to the QR code
    qrcode_url: QRCodeUrl
