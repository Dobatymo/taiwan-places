"""Print one catalogue ID using the shared library."""

from taiwan_places.random_id import create_uid, validate_uid

if __name__ == "__main__":
    uid = create_uid()
    print(uid)
    assert validate_uid(uid)
