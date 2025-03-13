
unweighted_graph = {
    "Maheshwari": ["Maheshwari Road", "Krantiveer Salve Marg"],
    "Maheshwari Road": ["Kondivita Road"],
    "Kondivita Road": ["Regent Hotel"],
    "Regent Hotel": ["OnTime Hotel"],
    "OnTime Hotel": ["ICICI Bank"],
    "ICICI Bank": ["BD Sawant Road", "Service Road"],
    "BD Sawant Road":["NS Phadke Road"],
    "NS Phadke Road" : ["S Radhakrishan Road"],
    "S Radhakrishan Road": ["Sahar Road"],
    "Sahar Road": ["Andheri Kurla Road"],
    "Andheri Kurla Road": ["MVLU"],
    "MVLU": [],

    "Service Road": ["Andheri Kurla Road"],
    "Krantiveer Salve Marg": ["Saraswat Bank"],
    "Saraswat Bank": ["Starwing Developers"],
    "Starwing Developers": ["Old Nagardas Road"],
    "Old Nagardas Road": ["MVLU"]
}

visited = []
queue = []

def bfs(visited,queue,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m,end =" \n")
        for neighbour in unweighted_graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,queue,"Maheshwari")
    

import networkx as nx
import matplotlib.pyplot as plt

# Given dictionary



#Choosing a Seed: You can choose any integer value for the seed parameter.
#The same seed value will produce the same layout each time it's used, while omitting the seed
#or using different seeds will result in different layouts.


# Create a directed graph
G = nx.DiGraph(unweighted_graph)

# Position the nodes using a spring layout with adjusted spacing
pos = nx.spring_layout(G, seed=42, k=0.4)  # Adjust 'k' for more or less spacing

# Draw the graph
plt.figure(figsize=(9, 6))  # Set the figure size for better readability
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
plt.title("Graph Representation of the Given Dictionary")
plt.show()
