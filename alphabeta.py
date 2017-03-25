import logicparse as lp

# class for a game tree, includes methods for adding a parent,
# adding children, performing alphabeta pruning
class abtree:
    def __init__(self, maxp, parent=None,value=None):
        self.max = maxp # max mode if true, min if false
        self.parent = parent
        self.value = value
        self.children = []
        self.leaves = 0 # number of leaves evaluated in alphabeta 

    # assigns parent
    def add_parent(self, parent):
        self.parent = parent

    # adds a child node to list of children
    def add_child(self, child):
        self.children.append(child)
    
    # calls the alphabeta algorithm as the root
    def root_ab(self):
        return self.alphabeta(float('-inf'), float('inf'))

    # evaluates the alphabeta scoring algorithm
    def alphabeta(self, alpha, beta):
        if not self.children:
            return self.value, 1

        if self.max:
            self.value = float('-inf')
            for child in self.children:
                v, leaves = child.alphabeta(alpha, beta)
                self.value = max(self.value, v)
                alpha = max(alpha, self.value)
                self.leaves += leaves
                if beta <= alpha: break
        else:
            self.value = float('inf')
            for child in self.children:
                v, leaves = child.alphabeta(alpha, beta)
                self.value = min(self.value, v)
                beta = min(beta, self.value)
                self.leaves += leaves
                if beta <= alpha: break

        return self.value, self.leaves

# generates a tree using the list of vertices and a list of edges
def gen_abtree(vertices, edges):
    nodes = {}
    for node in vertices:
        nodes[node[0]] = abtree(node[1] == 'MAX')

    for node in edges:
        if type(node[1]) == str:
            # add a child
            nodes[node[0]].add_child(nodes[node[1]])
            nodes[node[1]].add_parent(nodes[node[0]])
        else:
            # add a leaf with value node[1]
            nodes[node[0]].add_child(abtree(None, nodes[node[0]], node[1]))

    for node in nodes:
        # return the root
        if not nodes[node].parent: return nodes[node]

# reads in alphabeta.txt, performs alphabeta pruning, 
# writes results to alphabeta_out.txt
def main():
    f = open('alphabeta.txt', 'r')
    inp = f.readlines()
    f.close()

    results = []
    
    for line in inp:
        if line != '\n':
            inputs = lp.nestgen(lp.parse(line))
            tree = gen_abtree(inputs[0], inputs[1])
            results.append(tree.root_ab())

    f = open('alphabeta_out.txt', 'w')
    i = 1
    for result in results:
        f.write("Graph {}: Score: {}; Leaf Nodes Examined {}\n".format(i, result[0], result[1]))
        i += 1
    f.close()

if __name__ == '__main__':
    main()
