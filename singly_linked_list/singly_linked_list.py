# Create a Node class
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        # Because next_node is by default "None"
        # any given node is a tail by default
        self.next_node = next_node

    # Create class methods for manipulation of the nodes
    # Return current node value
    def get_value(self):
        return self.value

    # Return current pointer
    def get_next(self):
        return self.next_node

    # Set new pointer
    def set_next(self, new_next):
        self.next_node = new_next


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        # Check for head presence
        # If list is empty:
        if not self.head:
            # Make new_node the head and tail
            self.head = new_node
            self.tail = new_node
        # If list is not empty
        else:
            # Set current tail's reference to new_node
            self.tail.set_next(new_node)
            # Set new_node as the new tail
            self.tail = new_node

    def remove_head(self):
        # Return none if LL does not exist and LL is empty
        if not self.head:
            return None
        # Check if the head has a next
        # If no next, LL has a single element
        if not self.head.get_next():
            # Get the LL head
            head = self.head
            # Delete LL head
            self.head = None
            # Delete LL tail
            self.tail = None
            # Return result
            return head.get_value()
        # Get current head reference
        value = self.head.get_value()
        # Set new head to current head's next
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # Empty list
        if not self.head:
            return None
        # One element list
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        # Start at head
        current = self.head
        # Move through LL until the penultimate node where next = tail
        while current.get_next() is not self.tail:
            current = current.get_next()
        ########
        value = self.tail.get_value()
        # Set new tail to current node, previously penultimate
        self.tail = current
        return value

    def contains(self, value):
        # Empty list returns false
        if not self.head:
            return False
        # Start at head
        current = self.head
        # Iterate through LL to search for value
        while current:
            if current.get_value() == value:
                return True
            # Assuming current isn't desired value, move forward in LL
            current = current.get_next()
        # False if is not in list
        return False

    def get_max(self):
        # Empty list
        if not self.head:
            return None

        # Set initial max value = head value
        max_value = self.head.get_value()
        # Begin list iteration
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                # if new node > old max, update max
                max_value = current.get_value()
            current = current.get_next()
        return max_value
