
# nums = 123456789


# def descending_order(num):
#     # Bust a move right here
#     out = [int(x) for x in str(num)]
#     print(out)
#     sortedOut = out.sort(reverse=True)
#     print(sortedOut)
# descending_order(nums)

import re 

# with open('names.txt') as file:
#     data = file.readlines()
#     # print(data)
#     i = 0
#     for n in data:
#         pat = re.compile('(?P<first>[A-Z][a-zA-Z]+), (?P<last>[A-Z][a-zA-Z-]+)(?P<op>[\w\W]+)(?P<domain>)(?P<twitter>@[a-z]+)')
        
#         m = pat.search(data[i])
#         if m:
#             print(f"{m.group('first')} {m.group('last')} / {m.group('twitter')}")
#             i += 1
#         else:
#             print('None')
#             i += 1

with open('regex_test.txt') as file:
    data = file.readlines()
    # print(data)
    i = 0
    pat = re.compile('(?P<first>[A-Z][a-z]+) (?P<op>[A-Z]+|[A-Z][a-z]+) (?P<last>[A-Z][a-z]+)')
    for n in data:
        m = pat.search(data[i])
        if m:
            print(f"{m.group('first')}{m.group('op')}{m.group('last')}")
            i += 1
    else:
        print('None')
        i += 1
