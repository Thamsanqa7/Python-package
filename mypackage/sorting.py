def bubble_sort(items):
    """
    Return array of items, sorted in ascending order

    arg:
      items (int): list containing numerical values
    return:
       out (int): array of items sorted in ascending order
    """
    out = items.copy() # in place protection on items
    for n in range(len(out)):
        for m in range(len(out)-1-n):
            if out[m] > out[m+1]:
                out[m], out[m+1] = out[m+1], out[m]

    return out

def bubble_sort(items):
    """
    the quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    out = items.copy() # in place protection on items
    for n in range(len(out)):
        for m in range(len(out)-1-n):
            if out[m] > out[m+1]:
                out[m], out[m+1] = out[m+1], out[m]

    return out

def merge_sort(items):
  """
    the merge_sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    len_items = len(items)
    if len_items ==1:
        return items
    median_point = int(len_items / 2)
    items1=merge_sort(items[:median_point])
    items2=merge_sort(items[median_point:])

    def linear_merge(list1,list2):
        """
         return two lists merged and sorted in ascending order
        """
        sortd = []
        while (len(list1) >= 1 and len(list2) >= 1):
            if list1[0] < list2[0]:
                sortd.append(list1[0])
                list1.pop(0)
            else:
                sortd.append(list2[0])
                list2.pop(0)
        if len(list1) == 0:
            sortd = sortd + list2
        elif len(list2) == 0:
            sortd = sortd + list1
        return sortd
    return linear_merge(items1,items2)

def quick_sort(items):
    """
    the quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    len_items = len(items)

    if len_items <= 1:
        return items

    pivot = items[-1]
    small = []
    large = []
    dupl = []
    for n in items:
        if n < pivot:
            small.append(n)
        elif n > pivot:
            large.append(n)
        elif n == pivot:
            dupl.append(n)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dupl + large
