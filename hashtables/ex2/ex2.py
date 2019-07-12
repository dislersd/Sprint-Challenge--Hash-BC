#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    start = hash_table_retrieve(ht, 'NONE')
    route[0] = start

    for i in range(len(route) - 1):
        route[i + 1] = hash_table_retrieve(ht, route[i])

    return route

#    0      1       2      3     4      5      6      7      8
# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]


tickets = [
    Ticket("PIT",  "ORD"),
    Ticket("XNA",  "CID"),
    Ticket("SFO",  "BHM"),
    Ticket("FLG",  "XNA"),
    Ticket("NONE",  "LAX"),
    Ticket("LAX",  "SFO"),
    Ticket("CID",  "SLC"),
    Ticket("ORD",  "NONE"),
    Ticket("SLC",  "PIT"),
    Ticket("BHM",  "FLG")
]

print(reconstruct_trip(tickets, 9))
