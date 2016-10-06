import re

test = "/test/sdfsdf/hello/hiiiiee"

test = re.sub('/[^/]*$', '', test)

print(test)