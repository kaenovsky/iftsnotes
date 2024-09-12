import os
from pertchart import PertChart

# Construct the absolute path to the JSON file
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, 'pertdata.json')

# Load the PERT data and create the chart
pc = PertChart()
tasks = pc.getInput(json_path)
pc.create_pert_chart(pc.calculate_values(tasks))
