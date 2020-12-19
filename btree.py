
class BTree:
    def __init__(
        self,
        nivel: int = 3
    ):
        self.nivel = nivel
        self._max_keys = nivel - 1
        self._max_tam = self._max_keys * 2 + 1
        self.list = [None, None] * (self._max_keys) + [None]
        self._pos_elem = list(range(1, self._max_tam, 2))

    @property
    def _leaf(self):
        return self.count_depth == 1

    @property
    def count_depth(self):
        i = 0
        max_depth = 0
        while i < self._max_tam:
            if self.list[i]:
                max_depth = max(max_depth, self.list[i].count_depth)
            else:
                break
            i += 2
        return max_depth + 1

    @property
    def count_keys(self):
        return sum([1 for pos in self._pos_elem if self.list[pos]])

    @property
    def use_all_keys(self):
        return self._max_keys == self.count_keys

    def search(self, search_elem: int) -> bool:
        i = 1
        j = i + 2
        current_elem = self.list[i]
        if current_elem and search_elem < current_elem:
            if self.list[i-1]:
                return self.list[i-1].search(search_elem)
            else:
                return False

        while j < self._max_tam:
            next_elem = self.list[j]
            if current_elem:
                if current_elem == search_elem:
                    return True
                elif current_elem < search_elem:
                    if next_elem:
                        if search_elem < next_elem:
                            if self.list[i+1]:
                                return self.list[i+1].search(search_elem)
                            return False
                    elif self.list[i+1]:
                        return self.list[i+1].search(search_elem)
                i = j
                j += 2
                current_elem = next_elem
            else:
                return False

        if current_elem:
            if current_elem == search_elem:
                return True
            elif self.list[i+1]:
                return self.list[i+1].search(search_elem)
        return False

    def str_list(self):
        string = '{ '
        for i in range(self._max_tam):
            if i in self._pos_elem:
                if self.list[i]:
                    string += f'({self.list[i]}, {self.count_depth}) - '
            else:
                if self.list[i]:
                    string += self.list[i].str_list() + ' - '
        string += ' }'
        return string

    def print(self):
        string = '=====================\n'
        string += f'Nivel : {self.nivel}\n'
        string += 'To each elem: (Value, Height)\n'
        string += '=====================\n'
        string += self.str_list()
        string += '\n====================='
        print(string)

    def insert(self, elem):
        if self._leaf:
            list_elem = [self.list[i] for i in self._pos_elem if self.list[i]]
            list_elem += [elem]
            list_elem.sort()
            if not self.use_all_keys:
                i = 1
                for x in list_elem:
                    self.list[i] = x
                    i += 2
                return self
            else:
                half_pos = int(self._max_keys/2)
                half_elem = list_elem[half_pos]

                first_half = list_elem[:half_pos]

                left_node = BTree(self.nivel)
                for x in first_half:
                    left_node.insert(x)

                second_half = list_elem[half_pos+1:]

                right_node = BTree(self.nivel)
                for x in second_half:
                    right_node.insert(x)

                node = BTree(self.nivel)
                node.list[0] = left_node
                node.list[1] = half_elem
                node.list[2] = right_node

                return node
        else:
            i = 1
            while i < self._max_tam:
                current_elem = self.list[i]
                if current_elem:
                    if elem < current_elem:
                        break
                else:
                    break
                i += 2
            i -= 1
            before_node = self.list[i]
            node = self.list[i].insert(elem)
            if node.count_depth == before_node.count_depth :
                return self
            elif not self.use_all_keys:
                list_pos = list(range(self._max_tam-1, i, -1))
                for x in list_pos:
                    self.list[x] = self.list[x-2]
                self.list[i] = node.list[0]
                self.list[i+1] = node.list[1]
                self.list[i+2] = node.list[2]
                return self
            else:
                big_list = self.list + [None, None]
                list_pos = list(range(len(big_list)-1, i, -1))
                for x in list_pos:
                    big_list[x] = big_list[x-2]

                big_list[i] = node.list[0]
                big_list[i+1] = node.list[1]
                big_list[i+2] = node.list[2]

                half = int(self._max_tam/2)+1
                half_elem = big_list[half]
                if not isinstance(half_elem, int):
                    half -= 1
                    half_elem = big_list[half]

                first_half = big_list[:half]

                left_node = BTree(self.nivel)
                i = 0
                for x in first_half:
                    left_node.list[i] = x
                    i += 1

                second_half = big_list[half+1:]

                right_node = BTree(self.nivel)
                j = 0
                for x in second_half:
                    right_node.list[j] = x
                    j += 1

                node = BTree(self.nivel)
                node.list[0] = left_node
                node.list[1] = half_elem
                node.list[2] = right_node
                return node
