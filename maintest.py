import re

line = "User.all(" + "829018-23901-9283" + ")"
command = re.search(r"^(\w*)\.(\w+)\((\S*)\)", line)
# command = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)

a = command.group(1)
b = command.group(2)
c = command.group(3)


print(a)
print(b)
print(c)

