from functools import lru_cache
from urllib.request import urlopen, HTTPError
@lru_cache(maxsize=64)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urlopen(resource) as s:
            return s.read().decode("utf-8")
    except HTTPError:
        return 'Not Found'

while True:
    s = input("Give me PEP number?")
    if not s: break
    if not s.isdigit(): continue
    n = int(s)
    pep = get_pep(n)
    i = pep.find("PEP ")
    j = pep.find(" |", i)
    print(n, len(pep), pep[i:j])

print(get_pep.cache_info())
