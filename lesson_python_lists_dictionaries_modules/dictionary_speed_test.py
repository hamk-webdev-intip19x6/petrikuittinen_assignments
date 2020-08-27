import random
import string
import time

def random_string(sample_set, length):
    """Return random string of given length consisting of characters from sample set string"""
    return ''.join([random.choice(sample_set) for i in range(length)])

def random_phone_number():
    return random_string(string.digits, random.randint(7, 14))

def random_full_name():
    first_name = random_string(string.ascii_letters, random.randint(3, 10))
    last_name =  random_string(string.ascii_letters, random.randint(3, 20))
    return first_name + " " + last_name


def create_phone_numbers(n):
    phone_lookup = {}  # lookup table for phone number search
    name_lookup = {}   # lookup table for fullname search
    phone_list = []    # list containing all phone numbers
    name_list = []     # list containing all fullnames
    for i in range(n):
        phone_number = random_phone_number()
        full_name = random_full_name()
        phone_lookup[phone_number] = full_name
        name_lookup[full_name] = phone_number
        phone_list.append(phone_number)
        name_list.append(full_name)
    return phone_lookup, name_lookup, phone_list, name_list


if __name__ == "__main__":
    phone_lookup, name_lookup, phone_list, name_list = create_phone_numbers(10**5)
    time1 = time.time()
    for i in range(10**6):
        phone_number = random_phone_number()
        if phone_number in phone_lookup:
            print(phone_number, phone_lookup[phone_number])
    time2 = time.time()
    print("Time elapsed", time2-time1, "seconds")

    #for i in range(10**6):
    #    full_name = random.choice(
    ##    if full_name in name_lookup:
    #        print(full_name, name_lookup[full_name])
