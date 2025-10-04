from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for OIST mapping
oist_mappings = [
    {"id": 1, "name": "Mapping A", "description": "First mapping"},
    {"id": 2, "name": "Mapping B", "description": "Second mapping"}
]

@app.route('/oistmappings', methods=['GET'])
def get_oist_mappings():
    return jsonify(oist_mappings)

@app.route('/oistmappings/<int:mapping_id>', methods=['GET'])
def get_oist_mapping(mapping_id):
    mapping = next((m for m in oist_mappings if m["id"] == mapping_id), None)
    if mapping:
        return jsonify(mapping)
    return jsonify({"error": "Mapping not found"}), 404

@app.route('/oistmappings', methods=['POST'])
def create_oist_mapping():
    data = request.get_json()
    new_mapping = {
        "id": len(oist_mappings) + 1,
        "name": data.get("name"),
        "description": data.get("description")
    }
    oist_mappings.append(new_mapping)
    return jsonify(new_mapping), 201

if __name__ == '__main__':
    app.run(debug=True)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def find_min_in_tree(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val
# Example usage:
# Constructing a simple BST         
#       5
#      / \          
#     3   7
#    / \ / \
#   2  4 6  8

root = TreeNode(5)
root.left = TreeNode(3) 
root.right = TreeNode(7)
root.left.left = TreeNode(2)    
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print("Smallest element in the tree:", find_min_in_tree(root))
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def find_min_in_tree(root):

    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val
# Example usage:
# Constructing a simple BST                             