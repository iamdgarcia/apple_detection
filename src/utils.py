import json
import os

def save_results(results, output_dir,output_name):
    """Save detection results as a JSON file."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{output_name}.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)