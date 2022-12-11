class Graph: 
    # 그래프는 노드들의 리스트로 구성된다.
    def __init__(self, nodes_in_graph=[]):
        self.nodes_in_graph = nodes_in_graph

    def add_node(self, node):
        self.nodes_in_graph.append(node)

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def get_node(self, nodename):
        for node in self.nodes_in_graph:
            if node.nodename == nodename:
                return node

    def build_cost_tables(self):
        for node in self.nodes_in_graph:
            node.build_cost_table(self)

    def get_shortest_path(self, from_nodename, to_nodename):
        from_node = self.get_node(from_nodename)
        return from_node.get_shortest_path_to(to_nodename)

class Node:
    # connections is a dict of {nodename: cost}
    def __init__(self, nodename, connections):
        self.nodename = nodename
        self.connections = connections

        self.cost_table = {self.nodename: {'cost': 0, 'previous': None}}

        for name, cost in self.connections.items():
            self.cost_table[name] = {'cost': cost, 'previous': self.nodename}

    def __repr__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections: {self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'

    def __str__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections: {self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'

    def get_shortest_path_to(self, some_node_name):
        shortest_path = []
        costs = []
        total_cost = self.cost_table[some_node_name]['cost']
        current_node = some_node_name[:]

        for _ in range(10000):
            shortest_path.append(current_node)

            if self.cost_table[current_node]['previous'] != None:
                costs.append(self.cost_table[current_node]['cost'] - self.cost_table[self.cost_table[current_node]['previous']]['cost'])
    
            current_node = self.cost_table[current_node]['previous']

            if current_node == None:
                break

        costs = list(reversed([str(cost) for cost in costs]))

        return_str = ''

        for idx, let in enumerate(reversed(shortest_path)):
            if idx < len(costs):
                return_str += let + f' - {costs[idx]} -> '
            else:
                return_str += let
            
        return_str += f'\ntotal cost:{total_cost}'

        return return_str

    def build_cost_table(self, graph):
        # cost_table is a dict of {nodename: {'cost': cost, 'previous': previous_nodename}}
        visited = [self.nodename]

        for node in graph.nodes_in_graph:
            if node.nodename not in self.cost_table:
                self.cost_table[node.nodename] = {'cost': 10**9, 'previous': None}

        unvisited = [node.nodename for node in graph.nodes_in_graph if node.nodename != self.nodename]

        # 모든 노드를 방문할 때까지 반복
        for _ in range(100):
            # 가장 작은 cost를 가진 노드를 찾는다.
            min_cost, min_node = min([(self.cost_table[nodename]['cost'], nodename) for nodename in unvisited])

            min_node = graph.get_node(min_node)

            for nodename, cost in min_node.connections.items():
                dist_from_start = min_cost + cost

                if dist_from_start < self.cost_table[nodename]['cost']:
                    self.cost_table[nodename]['cost'] = dist_from_start
                    self.cost_table[nodename]['previous'] = min_node.nodename

                visited.append(min_node.nodename)

                if min_node.nodename in unvisited:
                    unvisited.remove(min_node.nodename)
            
            if len(unvisited) == 0:
                # 모든 노드를 방문했으면 종료
                break
        
if __name__ == '__main__':
    # 노드 생성
    A = Node('u', {'x': 5, 'w': 3, 'v': 7})
    B = Node('x', {'u': 5, 'w': 4, 'y': 7, 'z': 9})
    C = Node('w', {'u': 3, 'x': 4, 'v': 3, 'y': 8})
    D = Node('v', {'u': 7, 'w': 3, 'y': 4})
    E = Node('y', {'x': 7, 'w': 8, 'v': 4, 'z': 2})
    F = Node('z', {'y': 2, 'x': 9})

    # 그래프 생성
    graph = Graph()
    graph.add_nodes([A, B, C, D, E, F])
    
    # 그래프에 있는 모든 노드의 cost_table을 생성
    graph.build_cost_tables()
    print(graph.nodes_in_graph)

    # u에서 z까지의 최단 경로를 구한다.
    print(graph.get_shortest_path('u', 'z'))