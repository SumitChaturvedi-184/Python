from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


graph = {
    "Maheshwari": ["Maheshwari Road", "Krantiveer Salve Marg"],
    "Maheshwari Road": ["Kondivita Road"],
    "Kondivita Road": ["Regent Hotel"],
    "Regent Hotel": ["OnTime Hotel"],
    "OnTime Hotel": ["ICICI Bank"],
    "ICICI Bank": ["BD Sawant Road", "Service Road"],
    "BD Sawant Road": ["NS Phadke Road"],
    "NS Phadke Road": ["S Radhakrishan Road"],
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
queue = deque()

def bfs(visited,queue,start_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m = queue.popleft()
        print(m , end="\n")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,queue,"Maheshwari")


#graph plot
G = nx.DiGraph(graph)
# Draw the graph
pos = nx.spring_layout(G, seed=42)  # Position the nodes using a spring layout

# Adjust label positions
label_pos = {k: [v[1], v[1] - 0.08] for k, v in pos.items()}

nx.draw(G, pos, node_size=100, font_size=10, font_color='black')

plt.show()
