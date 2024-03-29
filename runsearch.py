import numpy
import os, sys
from General_Search import General_Search

try:
    if sys.argv[1]:
        print "Printing from ", sys.argv[1], "...\n"
except:
    print "Text file not provided. Printing from graph.txt file.\n"
# graph_file = "graph.txt"
# graph_file = "BonusGraph.txt"
# graph_file = "second_graph.txt"
try:
    if sys.argv[1]:
        graph_file = sys.argv[1]
        # print "Printing from ", sys.argv[1], "...\n"
except:
    graph_file = "graph.txt"

if ".txt" in graph_file:
    changes_txt_file = open(graph_file)
else:
    print "Wait! It's not a text file!\nEnter a proper text file as the argument. Eg- python runsearch.py Graph.txt"
    exit(0)
the_read_file = changes_txt_file.readlines()

lines = [line.rstrip(' ') for line in open(graph_file)]
connection_list = []
heuristic_list = []
flag = ""

for i in range(0, len(lines)):
    lines[i] = lines[i][:len(lines[i]) - 1]
    if lines[i] == "#####":
        flag = 'copy_to_heuristic'
    if flag == 'copy_to_heuristic':
        heuristic_list.append(lines[i])
    elif flag == "":
        connection_list.append(lines[i])

# print heuristic_list
del heuristic_list[0]
del heuristic_list[-1]

heuristic_dict = {}
for i in range(0, len(heuristic_list)):
    #     key = "'" + heuristic_list[i][:1] + "'"
    #     value = "'" + heuristic_list[i][2:] + "'"
    key = heuristic_list[i][:1]
    value = heuristic_list[i][2:]

    #     print key, value

    if key in heuristic_dict:
        heuristic_dict[key].append(value)
    else:
        heuristic_dict[key] = value
    heuristic_dict['G'] = 0.0 #Adding the goal heuristic value as we can assume G will
    #always be there in the dict
print "Heuristic Dictionary = \n", heuristic_dict
connection_dict = {}
for i in range(0, len(connection_list)):
    key, target, manhattan = connection_list[i].split(" ")
    # print key, target, manhattan
    #     key = connection_list[i][:1]
    #     target_city_value = connection_list[i][2:3]
    #     manhattan_value = connection_list[i][4:]
    #     print key, city_value, manhattan_value

    if key in connection_dict:  # Add city values cond later
        connection_dict[key][target] = manhattan
    # pass
    else:
        connection_dict[key] = {target: manhattan}
    if target in connection_dict:
        connection_dict[target][key] = manhattan
    else:
        connection_dict[target] = {key: manhattan}

# print connection_dict

print "Connection Dictionary = \n", connection_dict, "\n"
# print connection_dict['A'][0][1]

the_list = ["DFS", "BFS", "DLS", "IDS", "UCS", "GS", "A*", "Beam Search", "HCS"]
for item in the_list:
    print item
    General_Search(connection_dict, item, heuristic_dict=heuristic_dict)
    print "\n"
# General_Search(connection_dict, "A*", heuristic_dict=heuristic_dict)