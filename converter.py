symbols = "0123456789ABCDEF"


def convert_from_decimal(N, base):    
    div, mod = divmod(N, base)        
    return convert_from_decimal(div, base) + symbols[mod] if div else symbols[mod]


def main(current_numeral_system, value, new_numeral_system):		
	new_numeral_system = int(new_numeral_system)
	return convert_from_decimal(int(value), new_numeral_system)	


if __name__ == "__main__":
	result = main(
		10,
		input("Value: "),
		input("New numeral system (2..16): "))
	print("Answer:", result)
