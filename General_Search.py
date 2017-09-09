from Queue import PriorityQueue

def General_Search(connection_dict, search_method, *args):
    queue = [['S']]  # problem.initalState
    safety_count = 0
    local_flag = True #for IDS
    l_state_change = False
    depth_limit = 2
    if search_method == "IDS":
        print "L = 0"
    print "Expanded = ", queue[0][0]
    print "Queue = ", queue
    idl_depth_limit = 1

    while (len(queue) != 0 and safety_count < 25):
        if queue == None:
            return ["No path found!"]
        leftmost_of_queue = queue[0][0]


        if leftmost_of_queue == 'G':
            print "Goal Found! \n"
            return queue
        popped = queue.pop(0)
        # print "Expanding = ", leftmost_of_queue
        #         print "Q after popping = " , queue
        # print "Popped = ", popped
        key_to_expand = popped[0]
        #         current_depth +=1
        #         print "Key to expand = ",  key_to_expand

        if search_method == "DFS":
            opened_nodes = sorted(connection_dict[key_to_expand], reverse = True)
            for l in opened_nodes:
                if l != 'S' and l not in popped:
                    items_to_insert = [l] + popped
                    queue.insert(0, items_to_insert)

        elif search_method == "BFS":
            opened_nodes = sorted(connection_dict[key_to_expand])
            for l in opened_nodes:
                if l != 'S' and l not in popped:
                    items_to_insert = [l] + popped
                    queue.append(items_to_insert)

        elif search_method == "DLS":
            if len(popped) < depth_limit + 1:
                opened_nodes = sorted(connection_dict[key_to_expand], reverse = True)
                # print  "Opened Nodes = ", opened_nodes
                # print popped
                for l in opened_nodes:
                    # print "expanded elements = ", l
                    # print "l", l, " not in popped", popped, ":", l not in popped
                    if l != 'S' and l not in popped:
                        items_to_insert = [l] + popped
                        queue.insert(0, items_to_insert)

            else:
                # print "Nulling popped!"
                # popped = []
                pass

        elif search_method == "IDS":
            if idl_depth_limit == 1 and local_flag:
                print "L =", idl_depth_limit
                print "Expanded = ", popped[0]
                print "Queue = ", [popped]
                local_flag = False

            if len(popped) < idl_depth_limit + 1 and 'G' not in popped:
                opened_nodes = sorted(connection_dict[key_to_expand], reverse = True)
                for l in opened_nodes:
                    if l != 'S' and l not in popped:
                        items_to_insert = [l] + popped
                        # print "Items to insert =", items_to_insert
                        queue.insert(0, items_to_insert)
                        # print "Q after insert ", queue

            elif "G" not in popped:
                idl_depth_limit +=1
                l_state_change = True

        elif search_method == "UCS":
            print popped
            print "dsd***=", connection_dict[popped[0]].items()

        if l_state_change:
            queue = [['S']]

        print_queue_state(queue, connection_dict, search_method, l_state_change, idl_depth_limit)

        if l_state_change:
            l_state_change = False

        safety_count += 1

def cost_of_path(path, connection_dict):
    if len(path) in [0, 1]:
        return 0
    cost = 0
    for idx in range(0, len(path) - 1):
        cost += connection_dict[path[idx][0]][path[idx][1]]
    return cost

def print_queue_state(queue, connection_dict, search_method, l_state_change, idl_depth_limit):
    if search_method in ["DFS", "BFS", "DLS", "IDS"]:
        if search_method == "IDS":
            if l_state_change:
                print "\n"
                print "L =", idl_depth_limit

        if len(queue) != 0:
            print "Expanded = ", queue[0][0]
            print "Queue = ", queue
    elif search_method in ["UCS", "A*"]:
        if len(queue) != 0:
            print "Expanded =", queue[0][0]
            if search_method == "UCS":
                cost_of_paths = [cost_of_path(path, connection_dict) for path in queue]
                print "Queue =", [cost_of_paths[idx] + queue[idx] for idx in range(0, len(queue))]
            elif search_method == "A*":
                pass


# def ucs(connection_dict, start, goal):
#     visited = set()
#     queue = PriorityQueue()
#     queue.put((0, start))
#
#     while queue:
#         cost, node = queue.get()
#         print cost, node
#         if node not in visited:
#             visited.add(node)
#
#             if node == goal:
#                 return
#             for i in connection_dict[node]:
#                 if i not in visited:
#                     # print float(connection_dict[node][i])
#                     # print type()
#                     print "Value to insert to q", i
#                     total_cost = int(cost) + float(connection_dict[node][i])
#                     queue.put((total_cost, i))
#     return queue

