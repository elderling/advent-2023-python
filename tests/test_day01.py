from advent2023.day01 import file_to_lines, first_digit, last_digit, number_from_line, day01Solution

def test_file_to_lines():
	lines = file_to_lines("data/sample/day01.txt")
	assert len(lines) == 4

def test_first_digit():
	assert(first_digit('a12a')) == '1'

def test_last_digit():
	assert(last_digit('a12a')) == '2'

def test_number_from_line():
	assert(number_from_line('a12a')) == 12

def test_day01Solution():
	solution = day01Solution("data/sample/day01.txt")
	assert solution == 142