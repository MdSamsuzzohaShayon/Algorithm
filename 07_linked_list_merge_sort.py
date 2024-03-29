from utils.linkedlist import LinkedList


def merge_sort(linked_list):
    """
    :param linked_list: sorts a linked list in ascending order
    :return: a sorted linked list will be returned
        - Recursively divide the linked list into sublists containing a single node
        - Repeatedly merge the sublists to produce sorted sublists until on remains
    Runs in O(kn log n)
    """

    # Add a stoping condition - if the list lize is 1 or empty
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_helf, right_half = split(linked_list)
    left = merge_sort(left_helf)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    :param linked_list: divide the unsorted list at midpoint into sublist
    :return:
        1. Start off with single linked list and find the midpoint
        2. The node that comes after the node at midpoint is assigned to the head of newly created linkedlist
        3. Connection between the midpoint node and the one after is removed
    Swapping node  references, comparing values are constant time operation
    takes logarithmic O(k log n) times
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        # index method which finds the node we want by traversing the list
        # Every split operation incurs a big O(k) cost where k is the midpoint of the list
        # Overall splits take logarithmic time
        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges to linked list sorting by data in the nodes
    :param left:
    :param right:
    :return: A new merged list will be returned
    Run in linear O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node or either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
            # If the head node of right is None we are pass the tail
            # Add the tail from left the merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # obtain node data to perform comparison operation
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
                # If data on left is grater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current  = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged



l = LinkedList()
# Add each one to the head of the list
l.add(7)
l.add(4)
l.add(10)
l.add(3)
l.add(13)

print(l)
sorted_linkedlist = merge_sort(l)
print(sorted_linkedlist)
