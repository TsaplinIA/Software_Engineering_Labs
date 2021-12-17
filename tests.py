import converter

def test_error_in_current_numeral_system():
	assert converter.main("1", "7", "2") == "Wrong current numeral system"

def test_error_in_value():
	assert converter.main("10", "7edf", "2") == "Wrong value"

def test_error_in_new_numeral_system():
	assert converter.main("10", "7", "abc") == "Wrong new numeral system"

def test_from_10_to_2():
	assert converter.main("10", "7", "2") == "111"
	
def test_from_2_to_10():
	assert converter.main("2", "111", "10") == 7

def test_from_16_to_8():
	assert converter.main("16", "A2B", "8") == "5053"