phone_pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phone_pattern.search('800-555-1212').groups())


print(phone_pattern.search('800-555-1212-1234'))
'''
You should never “chain” the search() and groups() methods in production code.
If the search() method returns no matches, it returns None, 
not a regular expression match object. Calling None.
groups() raises a perfectly obvious exception: 
None doesn’t have a groups() method. 
'''
print(phone_pattern.search('800-555-1212-1234').groups())

phone_pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phone_pattern.search('800-555-1212-1234').groups())

phone_pattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phone_pattern.search('800 555 1212 1234').groups())
print(phone_pattern.search('80055512121234').groups())
print(phone_pattern.search('800 555 1212').groups())

phone_pattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

# VERBOSE
phone_pattern = re.compile(r'''
	# don't match beginning of string,
	# number can start anywhere
	(\d{3})    # area code is 3 digit (e.g. '800')
    \D*        # optional sperator is any number of non-digits
    (\d{3})    # trunk is 3 digit (e.g. '555')
    \D*        # optional sperator
    (\d*)      # extension is optional and can be any number of digits
    $          # end of string
	''', re.VERBOSE)

print(phone_pattern.search('work 1-(800) 555.1212 # 1234').groups())
print(phone_pattern.search('800-555-1212'))


