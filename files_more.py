"""
More file, exception and OS examples
"""
import csv, os, os.path


print(os.getcwd())
try:
    os.mkdir('temp')
except FileExistsError:
    pass

# create new files with same name but different extensions as files in current directory
file_names = [name for name in os.listdir('.') if not name.startswith('.') and not name.startswith('_')]
print(file_names)
os.chdir('temp')
for name in file_names:
    new_name = name[:name.find('.')] + '.JPG'
    with open(new_name, 'w'):
        pass
        print(new_name)

# rename .JPG to .jpeg
os.chdir('temp')
names = [name for name in os.listdir('.') if name.endswith('.JPG')]
for name in names:
    new_name = name[:name.find('.')] + '.jpeg'
    # print(new_name)
    os.rename(name, new_name)

# CSV reading, including handling header with next()
with open('data.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    header = next(reader)
    print("Header is {}".format(header))
    for line in reader:
        print(line)

# file (non-CSV) way
# for line in data_file:
#     print(line)
#     parts = line.split(',')
# data_file.close()

# non-local exception handling
def fn():
    raise NameError

try:
    fn()
except:
    print("got exception!")
