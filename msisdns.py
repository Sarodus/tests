import re


def check_number(prefix, length, msisdn):
    if not prefix:
        return True

    length = length or '5,13'
    max_length = max(map(int, length.split(',')))
    lprefix = len(prefix)

    if not msisdn.startswith(prefix):
        msisdn = '%s%s' % (prefix, msisdn)

    lmsisdn = len(msisdn)

    if lmsisdn > max_length:
        # print 'INPUT', msisdn
        # print 'NUMBER', msisdn[lprefix:]
        # print 'EXTRA DIGITS', msisdn[lprefix:][:lmsisdn - max_length]
        # print 'LENGTH MSISDN', lmsisdn
        # print 'MAX', max_length
        # print 'OVERFLOW', lmsisdn-max_length

        if not int(msisdn[lprefix:][:lmsisdn - max_length]):
            msisdn = '%s%s' % (prefix, msisdn[lprefix:][lmsisdn - max_length:])

    ''' Validate prefix and phone length '''
    if re.match('^(?=^'+prefix+')[0-9]{'+length+'}$', msisdn):
        return msisdn
    return False


# TEST
# (prefix, length, input, output)
numbers = [
    ('63', '12', '63555555555', False),
    ('63', '12', '630555555555', '630555555555'),
    ('63', '12', '6300555555555', '630555555555'),
    ('63', '12', '63000555555555', '630555555555'),

    ('63', '12', '555555555', False),
    ('63', '12', '0555555555', '630555555555'),
    ('63', '12', '00555555555', '630555555555'),
    ('63', '12', '000555555555', '630555555555'),
    ('63', '12', '0000555555555', '630555555555'),
    ('63', '12', '0001555555555', '631555555555'),

    ('63', '12', '555555555555555555555555', False),


    ('593', '12,13', '5935555555555', '5935555555555'),
    ('593', '12,13', '593555555555', '593555555555'),
    ('593', '12,13', '5930555555555', '5930555555555'),

    ('593', '12,13', '55555555555', False),
    ('593', '12,13', '5555555555', '5935555555555'),
    ('593', '12,13', '05555555555', '5935555555555'),
    ('593', '12,13', '005555555555', '5935555555555'),
    ('593', '12,13', '0005555555555', '5935555555555'),
    ('593', '12,13', '00005555555555', '5935555555555'),
]

for n in numbers:
    msisdn = check_number(*n[:-1])
    print 'RESULT', msisdn, msisdn == n[3]
    print '==================='
