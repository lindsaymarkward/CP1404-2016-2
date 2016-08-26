#
def is_valid_label(label):
    """
    Determine if the input label matches the requirements:
     labels must start with a capital, have at least 5 characters and at least one number
    :return: True if label is valid, otherwise False
    """
    if len(label) < 5:
        return False
    if not label[0].isupper():
        return False
    for char in label:
        if not char.isnumeric():
            return False
    return True

def test_is_valid_label():
    false_test_cases = ["label1", "invalid", "Abc"]
    true_test_cases = ["Label1", "Valid56", "Abcd6"]

    for case in false_test_cases:
        print("{} is {}".format(case, is_valid_label(case)))

    for case in true_test_cases:
        print("{} is {}".format(case, is_valid_label(case)))

test_is_valid_label()