### time complexity of algorithm o(n)
### space complexity of algorithm o(1)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value

class Link_list:

    def __init__(self):
        self.head = None

    def __eq__(self, other):
        if not isinstance(other, Link_list):
            # don't attempt to compare against unrelated types
            return False

        temp = self.head
        temp2 = other.head

        while temp is not None and temp2 is not None:
            if temp != temp2:
                return False
            temp = temp.next
            temp2 = temp2.next

        if temp2 is not None or temp is not None:
            return False
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def push_node(self, node_value):
        new_node = Node(node_value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        #### each of the temp, reversed, list_to_do occupy 1 space which means space complexity = 3 ~ o(1)


        ### if size of list is 0 or 1 do nothing
        if self.head is None or self.head.next is None:
            return

        list_to_do = self.head.next
        reversed = self.head
        reversed.next = None

        while (list_to_do != None):
            temp = list_to_do
            list_to_do = list_to_do.next
            temp.next = reversed
            reversed = temp

        self.head = reversed
        return
