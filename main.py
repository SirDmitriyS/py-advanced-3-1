class FlatIterator:
    
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    def __iter__(self):
        self.cur_item = 0
        self.cur_subitem = -1
        return self

    def __next__(self):
        self.cur_subitem += 1
        if self.cur_subitem >= len(self.list_of_list[self.cur_item]):
            self.cur_item += 1
            self.cur_subitem = 0
        if self.cur_item >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cur_item][self.cur_subitem]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()