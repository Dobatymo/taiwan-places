# Taiwan places Python library

From the repository root:

```console
uv sync --project python
uv run --project python python -m unittest discover -s python/tests
uv run --project python random_id.py
```

Import the shared ID functions after installing this package:

```python
from taiwan_places.random_id import create_uid, validate_uid

uid = create_uid()
assert validate_uid(uid)
```

IDs are `wdir` followed by 16 URL-safe Base64 characters, for 20 characters total. The payload contains 11 random bytes plus a CRC-8/CDMA2000 checksum. The prefix is defined by `PREFIX` in `random_id.py`; validation accepts only that prefix and rejects unprefixed IDs. The checksum detects accidental corruption; it is not authentication. Python 3.8 and later are supported.

The event rewrite writes IDs into the `2` version. The later promotion step replaces the original with that version, preserving IDs on subsequent rewrites.
