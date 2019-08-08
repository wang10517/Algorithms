class ListNode(object):
    def __init__(self, val, next=None):
        self. val = val
        self.next = next


class singlyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, e):
        if self.length == 0:
            self.head = ListNode(e)
            self.tail = self.head
        else:
            self.tail.next = ListNode(e)
            self.tail = self.tail.next
        self.length += 1

    def remove(self, e):
        if self.length == 0:
            return None
        if self.head.val == e:
            self.head = self.head.next
            self.length -= 1
            return

        hd = self.head
        while hd.next:
            if hd.next.val == e:
                hd.next = hd.next.next
                self.length -= 1
                return
            hd = hd.next
        return None

    def replace(self, old, new):
        if self.length == 0:
            return None
        if self.head.val == old:
            self.head.val = new
            return

        hd = self.head
        while hd.next:
            if hd.next.val == old:
                hd.head.val = new
                return
            hd = hd.next
        return None

    def __str__(self):
        hd = self.head
        result = []
        while hd:
            result.append('{} -> '.format(hd.val))
            hd = hd.next
        result.append('None')
        return ''.join(result)

    def __repr__(self):
        return "linkList with length {0} and repre {1}".format(self.length, str(self))

    def reverse(self):
        hd = self.head.next
        new_head = self.head
        new_tail = new_head
        while hd:
            clone = ListNode(hd.val)
            clone.next = new_head
            new_head = clone
            hd = hd.next
        self.head = new_head
        new_tail.next = None
        self.tail = new_tail
