class Node:

  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

# Method to fetch value
  def get_value(self):
    return self.value

# Method for the next node
  def get_next_node(self):
    return self.next_node

# Method to update the next node
  def set_next_node(self, next_node):
    self.next_node = next_node


# Instance of Node
customNode = Node(44)
print(customNode.get_value())
