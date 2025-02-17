from graphviz import Digraph

# Initialize graph
dot = Digraph('Zoo ER Diagram', format='png')

# Entities (rectangles)
dot.node('A', 'Animal\n--------------\n- Animal_ID (PK)\n- Species\n- Name\n- Age\n- Health_Status', shape='rectangle', color='lightblue')
dot.node('E', 'Exhibit\n--------------\n- Exhibit_ID (PK)\n- Name\n- Location\n- Capacity', shape='rectangle', color='lightgreen')
dot.node('K', 'Keeper\n--------------\n- Keeper_ID (PK)\n- Name\n- Hire_Date\n- Specialization', shape='rectangle', color='lightpink')

# Attributes (ellipses)
for attr in ['Animal_ID (PK)', 'Species', 'Name', 'Age', 'Health_Status']:
    dot.node(f'A_{attr}', attr, shape='ellipse')
    dot.edge(f'A_{attr}', 'A')

for attr in ['Exhibit_ID (PK)', 'Name', 'Location', 'Capacity']:
    dot.node(f'E_{attr}', attr, shape='ellipse')
    dot.edge(f'E_{attr}', 'E')

for attr in ['Keeper_ID (PK)', 'Name', 'Hire_Date', 'Specialization']:
    dot.node(f'K_{attr}', attr, shape='ellipse')
    dot.edge(f'K_{attr}', 'K')

# Relationships (diamonds)
dot.node('R1', 'lives in', shape='diamond', color='orange')
dot.node('R2', 'cares for', shape='diamond', color='orange')

# Connect entities with relationships
dot.edge('A', 'R1', label='N')
dot.edge('R1', 'E', label='1')

dot.edge('A', 'R2', label='M')
dot.edge('R2', 'K', label='N')

# Render and view the diagram
dot.render('zoo_er_diagram', view=True)

print("ER diagram saved as 'zoo_er_diagram.png'")
