"""URL-safe catalogue IDs: 88 random bits and a CRC-8/CDMA2000 checksum."""

import base64
import re
import secrets

from fastcrc import crc8

PREFIX = "wdir"


def create_uid() -> str:
    random_bytes = secrets.token_bytes(11)
    checksum = crc8.cdma2000(random_bytes)
    return PREFIX + base64.urlsafe_b64encode(random_bytes + bytes([checksum])).decode("ascii")


def validate_uid(value: str) -> bool:
    if not value.startswith(PREFIX):
        return False
    payload = value[len(PREFIX) :]
    if re.fullmatch(r"[A-Za-z0-9_-]{16}", payload) is None:
        return False
    data = base64.urlsafe_b64decode(payload)
    return crc8.cdma2000(data[:11]) == data[11]
