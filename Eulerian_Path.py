import random

def cycler(newStart_Pair, graph_dict, visited_pairs):
    newCycle = []
    new_pairs = []
    #current_pair = newStart_Pair # need to start current pair with pair inside visited pairs 
    newStart = (newStart_Pair.partition(':')[0])
    newCycle.append(newStart)

    #loop original cycle 
    for i in visited_pairs:
        if newStart == (i.partition(':')[0]):
            current_pair = i

    # ith to end
    for j in range(0, len(visited_pairs)):
        if current_pair == visited_pairs[j] and j < len(visited_pairs):
            for add in range(j, len(visited_pairs)):
                new_pairs.append(visited_pairs[add])
                newCycle.append((visited_pairs[add].partition(':')[2]))
    #start to ith
    for beg in range(0, len(visited_pairs)):
        if current_pair == visited_pairs[beg]:
            for end in range(0, beg):
                new_pairs.append(visited_pairs[end])
                newCycle.append((visited_pairs[end].partition(':')[2]))
    
    # add onto the original cycle
    current_pair = newStart_Pair

    while current_pair not in new_pairs:
        new_pairs.append(current_pair)
        current_node = (current_pair.rpartition(':')[2])
        newCycle.append(current_node)
        if len(graph_dict[current_node]) > 1:
            for s in range(0, len(graph_dict[current_node])):
                if str(current_node) + ":" + str(graph_dict[current_node][s]) not in new_pairs:
                    current_pair = str(current_node) + ":" + str(graph_dict[current_node][s])
                    break
        else: 
            current_pair = str(current_node) + ":" + str(graph_dict[current_node][0])
    
    
    
    return new_pairs, newCycle

def EulerianCycle(graph_dict):
    # dont visit same edge twice
    all_nodes = list(graph_dict.keys())
    all_edges = []
    start_node = random.choice(all_nodes)
    #start_node = 8
    cycle = []
    visited_pairs = []

    for sN in all_nodes:
        for sE in range(0, len(graph_dict[sN])):
            all_edges.append(str(sN) + ":" + str(graph_dict[sN][sE]))
    
    #put start node into first cycle

    current_pair = str(start_node) + ":" + str(graph_dict[start_node][0])

    current_node = start_node
    cycle.append(current_node)
    #while the next node is not in visited node, produce a random cycle

    
    while current_pair not in visited_pairs:
        visited_pairs.append(current_pair)
        current_node = current_pair.rpartition(':')[2]
        cycle.append(current_node)
        if len(graph_dict[current_node]) > 1:
            for s in range(0, len(graph_dict[current_node])):
                if str(current_node) + ":" + str(graph_dict[current_node][s]) not in visited_pairs:
                    current_pair = str(current_node) + ":" + str(graph_dict[current_node][s])
                    break
        else: 
            current_pair = str(current_node) + ":" + str(graph_dict[current_node][0])
        

    #created a random cycle       
    


    while all(value in visited_pairs for value in all_edges) == False:
        #select a node new start in Cycle with still unexplored edges
        for unexplored in cycle:
            for r in range(0, len(graph_dict[unexplored])):
                if (str(unexplored) + ":" + str(graph_dict[unexplored][r])) not in visited_pairs:
                    newStart_Pair = str(unexplored) + ":" + str(graph_dict[unexplored][r])
                    result = cycler(newStart_Pair, graph_dict, visited_pairs)
                    visited_pairs = result[0]
                    cycle = result[1]

    
    return cycle




text_file = input()
input_name = '/Users/sanghyunlee/Desktop/' + text_file

with open(input_name) as f:
    lines = f.readlines()

keys = []
values = []
graph_dictionary = {}

for i in lines:
    i = i.strip('\n')
    split = i.split(':')
    keys.append((split[0]))
    values.append(split[1].split())


#for val in values:
#    for iterate in range(0,len(val)):
#        val[iterate] = int(val[iterate])

for iter in range(0,len(keys)):
    graph_dictionary[keys[iter]] = values[iter]

result = EulerianCycle(graph_dictionary)


output = open('/Users/sanghyunlee/Desktop/practice' + text_file, 'w')
counter = 0
for i in result:
    counter = counter + 1
    output.write(str(i))

    if counter != len(result):
        output.write(" ")


output.close()
