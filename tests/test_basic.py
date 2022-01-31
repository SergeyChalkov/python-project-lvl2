from gendiff import generate_diff


def test_flat(flat_one, flat_two, output):
    result = generate_diff(flat_one, flat_two)
    assert result == output
