pattern = re.compile(
        '([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)\.([0-9]*) > ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)\.([0-9]*)')
for line in self.lines:
    res = pattern.search(line)
    if res:
        k = (res.group(1), res.group(3))