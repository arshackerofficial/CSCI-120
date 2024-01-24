print("test")

somestring = ["first thing", "2nd thing", "3rd thing"]
someotherstring = ["first other thing", "2nd other thing", "3rd other thing"]

output = {}
for astring in somestring:
    output.update({astring:someotherstring[somestring.index(astring)]})
    print(output)