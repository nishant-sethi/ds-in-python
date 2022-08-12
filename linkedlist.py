from typing import List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:

    def add_to_list(self, data):
        pass

    def delete_from_list(self):
        pass

    def print_list(self, head: Node):
        if self.is_list_empty(head):
            print('List is Empty')
        elif head.next is None:
            print(head.data)
        else:
            temp = head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
        print("\n")

    def get_node_at_index(self, index, head):
        if self.is_list_empty(head):
            print('List is Empty')
            return None
        if index == 0:
            return head
        else:
            count = 1
            temp = head
            while count != index:
                count += 1
                temp = temp.next
            return temp

    def is_list_empty(self, head):
        return head is None

    def search_node_in_list(self, data, head: Node) -> List[Node]:
        if self.is_list_empty(head):
            print('List is Empty')
            return None
        else:
            temp = head
            prev = head
            while temp is not None:
                if temp.data == data:
                    return prev, temp
                else:
                    prev = temp
                    temp = temp.next
            return None, None

    def get_length(self, head: Node) -> int:
        if head is None:
            return 0
        elif head.next is None:
            return 1
        else:
            length = 0
            temp = head
            while temp is not None:
                length += 1
                temp = temp.next
            return length


class SingleLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def add_to_end_of_list(self, data):
        node = Node(data)
        if super().is_list_empty(self.head):
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def delete_from_list(self, node: Node):
        prev_node, search_node = super().search_node_in_list(node, self.head)
        if search_node is None:
            print('Node doesn\'t exist in List \n')
        else:
            if search_node.next is None:
                prev_node.next = None
                del search_node
            else:
                prev_node.next = search_node.next
                del search_node

    def add_at_index_in_list(self, data, index, list_head):
        node = Node(data)
        length = super().get_length(list_head)
        print('length = ', length)
        if length < index:
            print('cannot insert at index greater than length of list')
        else:
            index_node = super().get_node_at_index(index, list_head)
            node.next = index_node.next
            index_node.next = node

    def print_list(self):
        super().print_list(self.head)


class DoubleLinkedList(LinkedList):

    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def add_to_end_of_list(self, data):
        node = Node(data)
        if super().is_list_empty(self.head):
            self.head = node
        else:
            temp: Node = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.previous = temp

    def add_at_index_in_list(self, data, index,list_head):
        node = Node(data)
        if super().get_length(list_head) < index:
            print('cannot insert at index greater than length of list')
        else:
            index_node = super().get_node_at_index(index,list_head)
            node.next = index_node.next
            node.previous = index_node
            index_node.next.previous = node
            index_node.next = node

    def delete_from_list(self, node: Node):
        prev_node, search_node = super().search_node_in_list(node,self.head)
        if not search_node:
            print('Node doesn\'t exist in List \n')
        else:
            search_node.previous.next = search_node.next
            search_node.next = prev_node
            del search_node

    def print_list(self):
        super().print_list(self.head)


class CircularLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def add_to_list(self):
        pass

    def delete_from_list(self):
        pass

    def print_list(self):
        super().print_list(self.head)

