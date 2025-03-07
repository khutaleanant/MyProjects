class Graph:
    def __init__(self, numvertex):
        # Initialize adjacency matrix with -1 (indicating no relationship)
        self.adjMatrix = [[-1] * numvertex for _ in range(numvertex)]
        self.numvertex = numvertex
        print(self.numvertex)
        self.products = {}
        # print(self.products)
        self.productslist = [None] * numvertex
        # print(self.productslist)

    def set_product(self, vtx, id):
        # Assign a product id with its corresponding index
        if 0 <= vtx < self.numvertex:
            self.products[id]= vtx
            # print(self.products)
            self.productslist[vtx] = id
            # print(self.productslist)    

           

    def set_relationship(self, frm, to, cost=0):
        # Get the product index using the product id
        frm = self.products[frm]
        print(frm)
        to = self.products[to]
        print(to)
        
        # Set the relationship in the adjacency matrix
        self.adjMatrix[frm][to] = cost
             
        
        # For undirected graph, also set the reverse direction
        self.adjMatrix[to][frm] = cost
       
    def get_products(self):
        # Return the list of products (IDs)
        return self.productslist
        

    def get_relationships(self):
        # Return a list of relationships (from product, to product, cost)
        relationships = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjMatrix[i][j] != -1:  # Check if there is a relationship
                    relationships.append((self.productslist[i], self.productslist[j], self.adjMatrix[i][j]))
        return relationships

    def get_matrix(self):
        # Return the adjacency matrix
        return self.adjMatrix


# Create a graph with 6 products
G = Graph(6)

# Set the products
G.set_product(0, 'Laptop')
G.set_product(1, 'Laptop Bag')
# G.set_product(2, 'Wireless Mouse')
# G.set_product(3, 'Keyboard')
# G.set_product(4, 'Headphones')
# G.set_product(5, 'Monitor')

# Set the relationships with associated costs (e.g., shipping cost, complementary product recommendation)
G.set_relationship('Laptop', 'Laptop Bag', 10)  # Buying a laptop comes with a discount for a laptop bag
# G.set_relationship('Laptop', 'Wireless Mouse', 15)  # Customers who buy a laptop may also buy a mouse
# G.set_relationship('Laptop', 'Headphones', 20)  # Customers who buy a laptop might want headphones
# G.set_relationship('Laptop', 'Monitor', 30)  # Monitor is a complement for laptop
# G.set_relationship('Keyboard', 'Wireless Mouse', 5)  # Customers who buy a keyboard may also buy a mouse
# G.set_relationship('Wireless Mouse', 'Headphones', 25)  # Mouse and headphones as complementary items

# Output the results
print("Products in the eCommerce Store:")
print(G.get_products())

# print("\nRelationships between Products (with Costs):")
print(G.get_relationships())

print("\nAdjacency Matrix of Product Relationships:")
for row in G.get_matrix():
    print(row)
