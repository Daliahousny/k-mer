#Yasmine Hossam 20198099 B2
#Dalia Hosny 20198028 B4
import networkx, matplotlib.pyplot as plot

def kmer(seq,k):
    kmers=[]
    for i in seq:
        for r in range(len(i)-k+1):
            mer=i[r:r+k]
            if mer not in kmers:
                kmers.append(mer)
    return kmers

def find_edges_nodes(seq,k):
    nodes=[]
    edges=[]
    i=0
    for st in seq:
        edges.append((st[i:+k-1], st[i+1:i+k]))
        nodes.append(st[i:i + k - 1])
        nodes.append(st[i + 1:i + k])
    i+=1
    return nodes,edges

def visualizeDBGraph(graph):
    dbGraph = networkx.DiGraph()
    dbGraph.add_nodes_from(graph['nodes'])
    dbGraph.add_edges_from(graph['edges'])
    networkx.draw(dbGraph, with_labels=True, node_size=1000)
    plot.show()

seq=["TTACGTT", "CCGTTA", "GTTAC", "GTTCGA", "CGTTC"]
mers=kmer(seq,5)
nodes, edges = find_edges_nodes(mers, 5)
print(nodes)
print(edges)
graph={}
graph["nodes"]=nodes
graph["edges"]=edges
visualizeDBGraph(graph)