"""
# DO THIS NOW

a) Write a Python function that takes a filename and returns how many lines are in the file.

b) Write another version that returns how many non-blank lines there are.

"""


def main():
    print("{} lines total, {} non-blank lines".format(count_lines_in_file("debugging.py"),
                                                      count_nonblank_lines_in_file("debugging.py")))


def count_lines_in_file(filename):
    file_object = open(filename, 'r')
    lines = file_object.readlines()
    file_object.close()
    number_of_lines = len(lines)
    return number_of_lines


def count_nonblank_lines_in_file(filename):
    number_of_lines = 0
    file_object = open(filename, 'r')
    for line in file_object:
        line = line.strip()
        if line != "":
            number_of_lines += 1
    file_object.close()
    return number_of_lines


main()
