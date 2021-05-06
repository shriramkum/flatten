def flatten_list(flatten):
    num = []
    while flatten:
        e = flatten.pop()
        if type(e) == list:
            flatten.extend(e)
        else:
            num.append(e)
    num.sort()
    return num
nested_list = [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
flat_list = flatten_list(nested_list)
set_tuple = set(flat_list)
flat_list = list(set_tuple)
print(flat_list)
