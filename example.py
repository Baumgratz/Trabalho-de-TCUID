## ----------------------------------------------------------------
## Use to example
from btree import BTree
## The class Count use to generate a element to insert in the BTree
class Count:
    count = 1

    @property
    def value(self):
        old_value = self.count
        self.add()
        return old_value

    def add(self, qtd = 3):
        self.count += qtd

## Shuffle a list
def shuffle(order_list : list):
    from random import randint

    n_times = randint(1, 10)
    tam = len(order_list)
    for _ in range(tam * n_times):
        pos_1 = randint(0, tam-1)
        pos_2 = randint(0, tam-1)
        aux = order_list[pos_1]
        order_list[pos_1] = order_list[pos_2]
        order_list[pos_2] = aux

def exemplo():
    # Nivel of BTree (>=3)
    nivel = 4
    b_tree = BTree(nivel)

    n_elem = 30
    count = Count()
    list_elem = [count.value for _ in range(n_elem)]

    shuffle(list_elem)

    print(f'List_elem : {list_elem}')

    # Insert elements in the BTree
    for elem in list_elem:
        print(f'Insert : {elem}')
        b_tree = b_tree.insert(elem)

    # Print BTree
    print(f'BTree(nivel = {b_tree.nivel})')
    b_tree.print()
    print('+++++++++++++++++++')

    # Search in BTree
    list_elem.sort()
    search_list = []
    dont_search_list = []
    for x in range(1, count.count):
        if b_tree.search(x):
            search_list.append(x)
        else:
            dont_search_list.append(x)
    print(f'Search list : {search_list}')
    print(f'Dont Search list : {dont_search_list}')
    print('-------------------')
    print(f'Search all elems? {search_list == list_elem}')
