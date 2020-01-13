DATA_DIR = '../input'


class Nodes:
    def __init__(self, name):
        self.name = name
        self.parent = ''
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent


objs = {}
root = ''

with open(f'{DATA_DIR}/6', 'r') as f:
    paths = f.readlines()
    for p in paths:
        parent, child = p.strip().split(')')
        if parent not in objs.keys():
            p_node = Nodes(parent)
            objs[parent] = p_node
        else:
            p_node = objs[parent]

        if child not in objs.keys():
            c_node = Nodes(child)
            objs[child] = c_node
        else:
            c_node = objs[child]

        p_node.add_child(c_node)
        c_node.set_parent(p_node)

        if parent == 'COM':
            root = p_node

ans = 0
node_list = [(root, 0)]
while node_list:
    node, cnt = node_list.pop()
    ans += cnt
    for c in node.children:
        # print(f'{c.name} orbits {node.name}')
        node_list.append((c, cnt + 1))
print(f'Question 1: {ans}')


def get_path(n: Nodes):
    p = []
    while n != root:
        n = n.parent
        p.append(n.name)
    p.reverse()
    print('->'.join(p))
    return p


my_path = get_path(objs['YOU'])
santa_path = get_path(objs['SAN'])

ind = 0
while True:
    my_node = my_path[ind]
    santa_node = santa_path[ind]
    if my_node == santa_node:
        ind += 1
    else:
        break

print(f'{len(my_path) - ind} + {len(santa_path) - ind}')


