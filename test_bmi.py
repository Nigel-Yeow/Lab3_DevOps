import Lab2_DevOps.bmi as BMI

def test_bmi_normal():
    result = BMI.calculate_bmi(height=1.85, weight=65)
    expected = 0
    assert(result == expected)

def test_bmi_under():
    result = BMI.calculate_bmi(height=1.85, weight=35)
    expected = -1
    assert(result == expected)

def test_bmi_over():
    result = BMI.calculate_bmi(height=1.85, weight=95)
    expected = 1
    assert(result == expected)