symbols = "0123456789ABCDEF"


def convert_from_decimal(N, base):    
    div, mod = divmod(N, base)        
    return convert_from_decimal(div, base) + symbols[mod] if div else symbols[mod]


def check_numeral_system(numeral_system):
	if not numeral_system.isdigit(): return None
	result = int(numeral_system)
	if result in range(2, 17): # [2, 16]
		return result
	else:
		return None


def check_value(value, numeral_system):
	s = symbols[:numeral_system]
	for char in value:
		if char not in s:
			return False
	return True


def main(current_numeral_system, value, new_numeral_system):
	current_numeral_system = check_numeral_system(current_numeral_system)
	if current_numeral_system == None:
		return "Wrong current numeral system"
	
	if not check_value(value, current_numeral_system):
		return "Wrong value"
	
	new_numeral_system = check_numeral_system(new_numeral_system)
	if new_numeral_system == None:
		return "Wrong new numeral system"
	
	if current_numeral_system == 10:
		return convert_from_decimal(int(value), new_numeral_system)
	else:
		in_decimal = int(value, current_numeral_system)
		if new_numeral_system == 10:
			return in_decimal
		else:
			return convert_from_decimal(in_decimal, new_numeral_system)	


if __name__ == "__main__":
	result = main(
		input("Current numeral system (2..16): "),
		input("Value: "),
		input("New numeral system (2..16): "))
	print("Answer:", result)
