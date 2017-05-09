import re

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

CONST_S = 'Copyright '
year = 'MCMXLVI'

print(re.search(pattern, year))



'''
Use grammar {N, M}
'''
thousand_pattern = '^M{0, 3}$'
pattern = '^M{0, 3}(CM|CD|D?C{0, 3})(XC|XL|L?X{0, 3})(IX|IV|V?I{0, 3})$'
print(re.search(pattern, 'MDLV'))


'''
Verbose regular expressions
'''
pattern = '''
^                    # beginning of string
M{0, 3}              # thousands - 0 to 3 Ms
(CM|CD|D?C{0, 3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                     #         or 500-800 (D, followed by 0 to 3 Cs)
(XC|XL|L?X{0, 3})    # tens - 90 (XC), 40 (XL), 0-30 (0 TO 3 Xs), 
                     #     or 50-80 (L, followed by 0 to 3 Xs)
(IX|IV|V?I{0, 3})    # ones - 9 (IX), 4(IV), 0-3 (0 to 3 Is),
                     #     0r 5 - 8 (V, followed by 0 to 3 Is)
$                    # ending of string
'''
print(re.search(pattern, 'M', re.VERBOSE))                     
print(re.search(pattern, 'M'))





