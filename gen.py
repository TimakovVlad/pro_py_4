import types

def flat_generator(nnested_list):
    stack = nnested_list[::-1]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])
        else:
            yield current

# if __name__ == '__main__':
#     nested_list = [
#         [['а', ['б', 'в']], 'г', 'д'],
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f'],
#         [1, 2, None],
#     ]
#
#     for item in flat_generator(nested_list):
#         print(item)


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()