def General_Search(connection_dict, search_method, *args):
    queue = [['S']]  # problem.initalState
    safety_count = 0
    local_flag = True
    l_state_change = False
    depth_limit = 2
    if search_method == "IDS":
        print "L = 0"
    print "Expanded = ", queue[0][0]
    print "Queue = ", queue, "\n\n"
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
                local_flag = False
            if len(popped) < idl_depth_limit + 1 and 'G' not in popped:
                opened_nodes = sorted(connection_dict[key_to_expand], reverse = True)
                for l in opened_nodes:
                    if l != 'S' and l not in popped:
                        items_to_insert = [l] + popped
                        queue.insert(0, items_to_insert)

            elif "G" not in popped:
                idl_depth_limit +=1
                l_state_change = True
                # queue = [['S']]
                # print "Expanded =", queue[0][0]
                # print "Queue =", queue
            else:
                pass

        if len(queue):
            print "Expanded = ", queue[0][0]
            print "Queue = ", queue
        if l_state_change:
            print "\n"
            queue = [['S']]
            print "L =", idl_depth_limit
            print "Expanded = ", queue[0][0]
            print "Queue =", queue
            l_state_change = False
        safety_count += 1


