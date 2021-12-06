el = ['()', '{}', '[]', '<>']
file_inp = open('input_file.txt', 'r')
inp = file_inp.read()



def func(x):
    if x == ".":
        return True
    for tmp in el:
        x = x.replace(tmp, '')
    if x != "." and all([tmp not in x for tmp in el]):
        return False
    return func(x)


file_out = open("out_file.txt", 'w')
if func(inp):
    file_out.write("YES")
else:
    file_out.write("NO")

file_out.close()
file_inp.close()
