from typing import List, Dict, Tuple, Union, Any

def is_negative(x: float) -> bool:
    return x < 0

def print_many(s: Union[str, int, float], n: int = 5) -> None:
    for i in range(n):
        print(s)

def multiply_list(a: List[float], n: float) -> List[float]:
    return [n*i for i in a]

d: Dict[str, Any] = {"key": "value", "key2": ("tuple", ), "key3": 13}
#d[123] = "bug"
print(is_negative(4))
#print(is_negative("bug"))
print_many(5)
#print_many("bug", 3.5)
print(multiply_list([1, 2.5, 3], 2.5))
#print(multiply_list([1, "bug", 3.14], 5))
#print(multiply_list([1, "cat", 3.14], "bug"))
