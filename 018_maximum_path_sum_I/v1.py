from __future__ import annotations
from functools import cache
from dataclasses import dataclass
from typing import Optional

# Use triangle2 for 018 and triangle3 for 067
# Would've thought more than caching would be needed,
# maybe pruning of some sort

file = "triangle3"

@dataclass
class Node:
    value: int
    left_child: Optional[Node] = None
    right_child: Optional[Node] = None
    
    def __repr__(self):
        if self.left_child and self.right_child:
            return f"{self.value=} {self.left_child.value=} {self.right_child.value=}"
        return f"{self.value=} (no children)"

    def __hash__(self):
        return id(self)


with open(file) as f:
    data = list(reversed([[int(n) for n in row.strip().split(" ")] for row in f.read().strip().split("\n")]))


# First create top row (remember we just flipped the triangle)
current_row = [Node(value=n) for n in data[0]]
# Now go down rows and link in previous nodes
for row in data[1:]:
    previous_row = current_row
    current_row = [Node(value=n, left_child=previous_row[i], right_child=previous_row[i+1]) for i, n in enumerate(row)]

top_node = current_row[0]


@cache 
def max_of_tree(node):
    if node.left_child and node.right_child:
        return node.value + max(max_of_tree(node.left_child), max_of_tree(node.right_child))
    return node.value

print(max_of_tree(top_node))
