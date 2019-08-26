import re
zip_re = re.compile(r"\d{5}")
print(zip_re.findall("Here are some zip codes: 11100 and 11130"))
phone_re = re.compile(r"(\d{2,4})-(\d{1,10})")
print(phone_re.match("050-1234567").groups()) # ('050', '1234567')
print(phone_re.match("050-1234567").group(0)) # '050-1234567'
print(phone_re.match("050-1234567").group(1)) # '050'
print(phone_re.match("050-1234567").group(2)) # '1234567'
phone_re = re.compile(r"(?P<operator>\d{2,4})-(?P<number>\d{1,10})")
print(phone_re.match("050-1234567").groups()) # ('050', '1234567')
print(phone_re.match("050-1234567").group(0)) # '050-1234567'
print(phone_re.match("050-1234567").group(1)) # '050'
print(phone_re.match("050-1234567").group("operator"))
print(phone_re.match("050-1234567").group(2)) # '1234567'
print(phone_re.match("050-1234567").group("number"))


