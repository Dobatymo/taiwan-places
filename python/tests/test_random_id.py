import base64
import unittest
from unittest.mock import patch

from taiwan_places import random_id


class RandomIdTests(unittest.TestCase):
    def test_reference_format_and_checksum(self):
        expected = "wdir" + base64.urlsafe_b64encode(bytes(11) + b"\x96").decode("ascii")
        with patch.object(random_id.secrets, "token_bytes", return_value=bytes(11)) as token_bytes:
            self.assertEqual(random_id.create_uid(), expected)
        token_bytes.assert_called_once_with(11)
        self.assertTrue(random_id.validate_uid(expected))

    def test_invalid_ids(self):
        payload = base64.urlsafe_b64encode(bytes(11) + b"\x96").decode("ascii")
        for value in (
            "",
            payload,
            "wd" + payload,
            "WDIR" + payload,
            "xx" + payload,
            "wdir" + payload + "=",
            *("wdir" + invalid for invalid in ("a" * 15, "a" * 17, "=" * 16, "+" * 16, "é" * 16, "A" * 16)),
        ):
            with self.subTest(value=value):
                self.assertFalse(random_id.validate_uid(value))

    def test_generated_ids(self):
        ids = {random_id.create_uid() for _ in range(256)}
        self.assertEqual(len(ids), 256)
        self.assertTrue(all(value.startswith("wdir") and len(value) == 20 for value in ids))
        self.assertTrue(all(random_id.validate_uid(value) for value in ids))


if __name__ == "__main__":
    unittest.main()
