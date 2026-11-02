import price_info as price
print("Test Price Info")

def test_total_cost_shopping():
    expected = 46.75
    result = price.total_cost_shopping()
    assert(result == expected)

def test_cost_of_fruits():
    expected = 49.5
    result = price.cost_of_fruits('pomegranate', 10)
    assert(result == expected)