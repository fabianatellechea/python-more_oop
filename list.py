#!/usr/bin/python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f'Added: {item}')

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f'Removed: {item}')
        else:
            print('Item not found')

verbose_list = VerboseList()

verbose_list.append(1)
verbose_list.append(2)
verbose_list.append(3)
verbose_list.remove(2)
verbose_list.remove(4)