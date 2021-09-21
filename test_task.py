'''
Задание по Python
Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
-----------
Task: make a function to build a tree from list of tuples (id parent, id child) 
where None is root node
-----
Пример работы:
'''
source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def foundkey(fk,tr,level=0):
    #print('searching ',fk,' in ',tr, ' level:',level)
    if fk in tr:
        #print("found ")
        return tr[fk]

    for k in tr:
        fnd = foundkey(fk, tr[k] , level=level+1)
        if fnd != None:
            return fnd

    return None

def to_tree(source):
    tree = {}
    for i in source:
        if i[0] is None:
            tree[i[1]] = {}
        else:
            fkey = foundkey(i[0],tree)
            if fkey != None:
                fkey[i[1]] = {}
            else:
                print('not found key: ',i[0],)

    return tree


dic1 = to_tree(source)
if dic1==expected :
    print('dict is ok')

