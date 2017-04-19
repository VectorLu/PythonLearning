def not_empty(s):
    return s and s.strip()

no_blank = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(no_blank)
