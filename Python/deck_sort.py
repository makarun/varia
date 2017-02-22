def deck_sort(A):
    my_order = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    order = {key: i for i, key in enumerate(my_order)}
    return sorted(A, key=lambda d: order[d])

