log = open('/var/log/dpkg.log').read()
print log

import re
#print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)

print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)