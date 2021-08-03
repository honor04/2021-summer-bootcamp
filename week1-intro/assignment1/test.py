def to_upper_case(words: [str]) -> [str]:
    upper = list(map(lambda x: x.upper(), words))
    return upper


assert to_upper_case(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]

def to_upper_case_wrong(words: [str]) -> [str]:
    return list(map(lambda x: x.upper(), words))


assert to_upper_case_wrong(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case_wrong(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]