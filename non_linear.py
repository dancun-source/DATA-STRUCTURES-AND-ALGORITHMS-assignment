# 1. TREE (Hierarchical)
class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val

# 2. GRAPH (Interconnected)
# Represented as an Adjacency List
graph = {
    'NodeA': ['NodeB', 'NodeC'],
    'NodeB': ['NodeA'],
    'NodeC': ['NodeA']
}
