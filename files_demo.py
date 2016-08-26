
# in_file = open("textfile.txt", "r")
# text = in_file.readline()
# print(text)
# for line in in_file:
#     print("* ", repr(line))
# in_file.close()

out_file = open("textfile.txt", "a")
# print("96", file=out_file, end='')
out_file.write("hello\n")
out_file.close()