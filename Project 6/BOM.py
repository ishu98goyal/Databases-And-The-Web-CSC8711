import sys
from py2neo import Graph

g = Graph(auth=(sys.argv[1], sys.argv[2]))

def menu():
    print('''
(c) cost of part
(s) sub-parts
(q) quit
    ''')
    return input('What do you want to see: ')


# All PARTS
def compute_part_cost(part_node):
    if part_node["type"] == "basic":
        # if the part is basic, return its price
        return part_node["price"]
    else:
        # if the part is complex, compute the cost of its subparts
        subparts_cost = 0
        for subpart_rel in g.match((part_node, ), r_type="subpart"):
            subpart_node = subpart_rel.end_node
            subpart_qty = subpart_rel["qty"]
            subpart_cost = compute_part_cost(subpart_node)
            subparts_cost += subpart_qty * subpart_cost
        return subparts_cost


#Part Cost

def part_cost(part_name):
    part_node = g.nodes.match("Part", name=part_name).first()
    part_cost = compute_part_cost(part_node)
    print(f"\nCost of {part_node['name']} is: {part_cost:.1f}\n")

#Subpart Cost
prev_qty = 1
def subparts_count(part_name):
    part_node = g.nodes.match("Part", name=part_name).first()
    quantity = {}

    def compute_subparts_count(part_node, qty):
        if part_node["type"] == "basic":
            quantity[part_node['name']] = quantity.get(part_node['name'], 0) + qty
        else:
            for subpart_rel in g.match((part_node, ), r_type="subpart"):
                subpart_node = subpart_rel.end_node
                subpart_qty = subpart_rel["qty"]
                prev_qty = qty
                compute_subparts_count(subpart_node, prev_qty*subpart_qty)

    compute_subparts_count(part_node, 1)
    print(f'\nSubparts of part {part_node["name"]} are: ')
    for key in quantity.keys():
        print(f'{key}  {quantity[key]}')



# MAIN
user_choice = menu()
while user_choice != 'q':
    part_name = input('Enter the part name: ')
    if user_choice == 'c':
        part_cost(part_name)
    if user_choice == 's':
        subparts_count(part_name)
    user_choice = menu()