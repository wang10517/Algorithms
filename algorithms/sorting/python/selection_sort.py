from data_structure.linklist.doublyLinkedList import doublyLinkedList, ListNdoe


def selection_sort(arr, comparator_func):

    buffer = []
    doubly_list = doublyLinkedList()
    while arr:
        cur = arr.pop()
        list_ptr = doubly_list.head
        while list_ptr and list_ptr.val < cur:
            list_ptr = list_ptr.next
        node = ListNdoe(cur)
        if list_ptr:
            if not list_ptr.prev:
                doubly_list.head = node
            else:
                list_ptr.prev.next = node
            node.prev = list_ptr.prev
            node.next = list_ptr
            list_ptr.prev = node
            doubly_list.length += 1
        else:
            doubly_list.add(cur)

    doubly_list.printList()


selection_sort([3, 2, 1], (lambda x, y: x < y))
selection_sort([3, 2, 1, 257, 32, 58], (lambda x, y: x < y))
