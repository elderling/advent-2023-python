def file_to_lines(filename : str):
	with open(filename) as f:
		lines = f.readlines()
	return lines

def first_digit( s : str ):
	for c in s:
		if c.isdigit():
			return c
	return ''

def last_digit( s : str ):
	return first_digit(reversed(s))

def number_from_line( line : str ):
	return int(first_digit(line)) * 10 + int(last_digit(line))

def day01Solution( filename : str ):
	lines = file_to_lines(filename)
	sum = 0
	for line in lines:
		sum += number_from_line(line)
	return sum