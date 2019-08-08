class ListNdoe(object):
    def __init__(self, val, next=None, prev=None):
        self. val = val
        self.next = next
        self.prev = prev


class doublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, e):
        if not self.length:
            self.head = ListNdoe(e)
            self.tail = self.head
        else:
            node = ListNdoe(e)
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.length += 1

    def remove(self, e):
        if self.head.val == e:
            self.head = self.head.next
            self.head.prev = None
        else:
            hd = self.hd
            while hd.next:
                hd = hd.next
                if hd.val == e:
                    hd.prev.next = hd.next
                    if hd.next:
                        hd.next.prev = hd.prev
        self.length -= 1

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
            result.append('{} <=> '.format(hd.val))
            hd = hd.next
        result.append('None')
        return ''.join(result)

    def __repr__(self):
        return "linkList with length {0} and repre {1}".format(self.length, str(self))
