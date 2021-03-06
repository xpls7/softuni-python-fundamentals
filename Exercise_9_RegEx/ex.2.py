import re

data = input()

pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"

result = [el.group() for el in re.finditer(pattern, data)]

print(",".join(result))
