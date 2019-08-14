from itertools import combinations

def validify_tickets(tickets, n, k, l):
    """
        tickets: a set of stickets to be validified
        n : the list of numbers narrowed down 
        k : the number of slots in each ticket
        l : the minimum number of tickets required to win a prize
    """
    all_sets = combinations(n, k)
    for s in all_sets:
        found = False
        for ticket in tickets:
            if len(set(ticket).intersection(s)) >= l:
                found = True
                break
        if not found:
            return False
    return True
                

print(validify_tickets([[1,2,3], [1,4,5]], [1,2,3,4,5], 3,2))
