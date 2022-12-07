import networkx as nx

def main():
    G = nx.Graph()
    file = open('12-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()

    for line in lines:
        node1, node2 = line.split('-')
        G.add_edge(node1, node2)
        
    paths = nx.all_simple_paths(G, "start", "end")
    # print(G.adj['start'])
    # for path in paths: 
    #     print(path)

if __name__ == "__main__":
    main()