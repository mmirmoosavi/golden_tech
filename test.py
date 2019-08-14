import unittest
from reverse_linklist import Node, Link_list

class Test_reverse(unittest.TestCase):

    def test_reverse_list(self):
        link_list_obj = Link_list()
        for i in range(1, 11):
            link_list_obj.push_node(Node(i))

        link_list_obj_reverse = Link_list()
        for i in range(10, 0, -1):
            link_list_obj_reverse.push_node(Node(i))


        link_list_obj.reverse()
        link_list_obj_reverse.print_list()
        link_list_obj.print_list()

        self.assertEqual(link_list_obj_reverse, link_list_obj)

    def test_another_list(self):

        link_list_obj = Link_list()
        for i in range(1, 11):
            link_list_obj.push_node(Node(i))

        other_list_obj = Link_list()
        for i in range(-1, 11):
            other_list_obj.push_node(Node(i))

        self.assertEqual(link_list_obj, other_list_obj)

if __name__ == '__main__':
    unittest.main()