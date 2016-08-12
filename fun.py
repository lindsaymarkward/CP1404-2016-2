NUM = 4

# Who can vote?

def main():
    print("Welcome")
    name, age, is_enrolled = get_details()
    if can_vote(age, is_enrolled):
        print("{} is {} and can vote".format(name, age))
    else:
        print("{} is {} and can NOT vote".format(name, age))

def get_details():
    name = input("Name: ")
    age = int(input("Age: "))
    enrolment_String = input("Are you enrolled (Y/N)").upper()
    is_enrolled = enrolment_String == "Y"

    return name, age, is_enrolled

def can_vote(age, is_enrolled):
    return age >= 18 and is_enrolled

main()


def multiply_string(text, number):
    return
    if number > 0:
        return text * number
    else:
        return "No"



def print_in_uppercase(text):
    """
    Print text in uppercase
    :param text: text to uppercase
    :return: None
    """
    text = text.upper()
    print(text * NUM)

text = "bob is sad"

# x = multiply_string(text, NUM)
# print(multiply_string(multiply_string("hello", 3), NUM))