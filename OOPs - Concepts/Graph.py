class Graph:
    def __init__(self, numvertex):
        # Initialize adjacency matrix with -1 (indicating no edge)
        self.adjMatrix = [[-1] * numvertex for _ in range(numvertex)]
        # print(self.adjMatrix)
        self.numvertex = numvertex
        print(self.numvertex)
        self.vertices = {}
        self.verticeslist = [None] * numvertex
        # print(self.verticeslist)

    def set_vertex(self, vtx, id):
        # Assign a vertex id with its corresponding index
        if 0 <= vtx < self.numvertex:
            self.vertices[id] = vtx
            print(self.vertices)
            
            self.verticeslist[vtx] = id
            print(self.verticeslist)

    def set_edge(self, frm, to, cost=0):
        # Get the vertex index using the vertex id
        frm = self.vertices[frm]
        to = self.vertices[to]
        
        # Set the edge in the adjacency matrix
        self.adjMatrix[frm][to] = cost
        print(self.adjMatrix)
        # For undirected graph, also set the reverse direction
        self.adjMatrix[to][frm] = cost
        print(self.adjMatrix)

    def get_vertex(self):
        # Return the list of vertices (IDs)
        return self.verticeslist

    def get_edges(self):
        # Return a list of edges (from vertex, to vertex, cost)
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjMatrix[i][j] != -1:  # Check if there is an edge
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        # Return the adjacency matrix
        return self.adjMatrix


# Create a graph with 6 vertices
G = Graph(6)



# # Set the vertices
# G.set_vertex(0, 'a')
# G.set_vertex(1, 'b')
# G.set_vertex(2, 'c')
# G.set_vertex(3, 'd')
# G.set_vertex(4, 'e')
# G.set_vertex(5, 'f')

# # Set the edges with associated costs
# G.set_edge('a', 'b', 5)
# G.set_edge('a', 'c', 20)
# G.set_edge('c', 'b', 30)
# G.set_edge('b', 'e', 40)
# G.set_edge('e', 'd', 50)
# G.set_edge('f', 'e', 60)

# # Output the results
# print("Vertices of Graph:")
# print(G.get_vertex())

# print("\nEdges of Graph:")
# print(G.get_edges())

# print("\nAdjacency Matrix of Graph:")
# for row in G.get_matrix():
#     print(row)
