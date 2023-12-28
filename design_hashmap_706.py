class MyHashMap:

    def __init__(self):
        self.map_size = 10000
        self.map = [[]]*self.map_size

    def _hash(self, key):
        return key%self.map_size    

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        inputs_at_index = self.map[index]
        for ind, rec in enumerate(inputs_at_index):
            if key == rec[0]:
                inputs_at_index[ind][1] = value
                return
        self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        inputs_at_index = self.map[index]
        for ind, rec in enumerate(inputs_at_index):
            if key == rec[0]:
                return rec[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        inputs_at_index = self.map[index]
        for ind, rec in enumerate(inputs_at_index):
            if key == rec[0]:
                self.map[index] = inputs_at_index[:ind] + inputs_at_index[ind+1:]