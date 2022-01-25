from gendiff import generate_diff


REQUIRED = """{
  - follow: false,
    host: hexlet.io,
  - proxy: 123.234.53.22,
  - timeout: 50,
  + timeout: 20,
  + verbose: true
}"""
FLAT_ONE = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
FLAT_TWO = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

result = generate_diff(FLAT_ONE, FLAT_TWO)

def test_flat():
    assert result == REQUIRED
