#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)
        # [ 4 (0), 6(1), 10(2), 15(3), 16(4) ]
    for i in range(0, len(weights)):
        value = hash_table_retrieve(ht, limit - weights[i])
        if value:
            return (value, i)
    return None


def print_answer(answer):
    if answer is not None:
        return (f'{answer[0]}, {answer[1]}')
    else:
        return ("None")

weights = [ 4, 6, 10, 15, 16 ]
print(get_indices_of_item_weights(weights, 5, 21))