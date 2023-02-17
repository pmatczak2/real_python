from collections import Counter
from collections import defaultdict
def majority_element_indexes(lst):
    """
    Return a list of the indexs of the majority element. Majority element is
    the element that appears more than floor(
    n / 2) times. If there is no majority element, return []
    >>> majority_element_indexes([1,1,2])
    [0, 1]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    """
    if lst == []:
        return []
    count = Counter(lst)
    top_elms = sorted(count.keys(), key=lambda x: -count[x])

    maj_elem = top_elms[0]
    if count[maj_elem] > len(lst) // 2:
        return [i for i, elem in enumerate(lst) if elem == maj_elem]
    else:
        return []