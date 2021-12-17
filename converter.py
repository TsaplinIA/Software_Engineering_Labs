symbols = "0123456789ABCDEF"


def convert_from_decimla(N, base):    
    div, mod = divmod(N, base)        
    return convert_from_decimal(div, base) + symbols[mod] if div else symbols[mod]


def main(current_numeral_system, value, new_numeral_system):
	current_numeral_system = int(current_numeral_system)
	new_numeral_system = int(new_numeral_system)
	
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
