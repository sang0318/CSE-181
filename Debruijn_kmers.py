def debruijn_adjacent(patterns_list):
    k = len(patterns_list[0])
    collection = {}
    for pattern in patterns_list:
        prefix = pattern[0:k-1]
        suffix = pattern[1:k]
        if prefix in collection:
            collection[prefix].append(suffix)
        else:
            collection[prefix] = [suffix]

    return collection

#patterns = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']

text_file = input()
input_name = '/Users/sanghyunlee/Desktop/' + text_file

with open(input_name) as f:
    lines = f.readlines()

patterns = lines[0].split()


result = debruijn_adjacent(patterns)

sorted = list(result.keys())
sorted.sort()
sorted_result = {key: result[key] for key in sorted}

for keys in sorted_result:
    sort_values = sorted_result[keys]
    if (len(sort_values) > 1):
        sort_values.sort()

output = open('/Users/sanghyunlee/Desktop/practice' + text_file, 'w')
for i in sorted_result:

    output.write(i)
    output.write(": ")
    for j in range(0, len(sorted_result[i])):
        output.write(sorted_result[i][j])
        if j != (len(sorted_result[i]) - 1):
            output.write(" ")
    if i != list(sorted_result.keys())[-1]:
        output.write("\n")


output.close()
