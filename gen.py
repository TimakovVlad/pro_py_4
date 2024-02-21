def flat_generator(nnested_list):
    stack = nnested_list[::-1]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])
        else:
            yield current

if __name__ == '__main__':
    nested_list = [
        [['а', ['б', 'в']], 'г', 'д'],
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    for item in flat_generator(nested_list):
        print(item)
