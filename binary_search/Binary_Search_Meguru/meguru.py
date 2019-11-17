"""Ref
https://twitter.com/meguru_comp/status/697008509376835584
https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
from typing import List, Callable


def binary_search_meguru_recur(f: Callable[[int], bool], ok: int, ng: int) -> int:
    """General purpose binary search algorithm

    Parameters
    ----------
    f : Callable[[int], int]
    ok : int
    ng : int

    Returns
    -------
    int
    """
    edge = ok

    def search(ok, ng):
        mid = (ok + ng) // 2
        return (
            ok if abs(ok - ng) <= 1 else
            search(mid, ng) if f(mid) else
            search(ok, mid)
        )
    ok = search(ok, ng)
    return ok if ok != edge else -1


def binary_search_meguru(f: Callable[[int], bool], ok: int, ng: int) -> int:
    """General purpose binary search algorithm

    Parameters
    ----------
    f : Callable[[int], int]
    ok : int
    ng : int

    Returns
    -------
    int
    """
    edge = ok
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok if ok != edge else -1


def lower_bound(arr: List[int], target: int) -> int:
    """Find the mimimun/leftmost element x in arr that satisfies x >= target 

    Parameters
    ----------
    arr : List[int]
        sorted array
    target : int

    Returns
    -------
    int
        index of the minimum element. -1 if all the elements are less than target
    """
    ng, ok = -1, len(arr)
    return binary_search_meguru(lambda x: arr[x] >= target, ok, ng)


def upper_bound(arr: List[int], target: int) -> int:
    """Find the maximum/rightmost element x in arr that satisfies x <= target 

    Parameters
    ----------
    arr : List[int]
        sorted array
    target : int

    Returns
    -------
    int
        index of the minimum element. -1 if all the elements are more than target
    """
    ng, ok = len(arr), -1
    return binary_search_meguru(lambda x: arr[x] <= target, ok, ng)


def find_leftmost(arr: List[int], target: int) -> int:
    lb = lower_bound(arr, target)
    return lb if (lb == -1 or arr[lb] == target) else -1


def find_rightmost(arr: List[int], target: int) -> int:
    ub = upper_bound(arr, target)
    return ub if (ub == -1 or arr[ub] == target) else -1


def find_closest(arr: List[int], target: int) -> int:
    """Return the leftmost closest elemnet

    Parameters
    ----------
    arr : List[int]
    target : int

    Returns
    -------
    int
    """
    ub = upper_bound(arr, target)
    lb = lower_bound(arr, target)
    if ub == -1:
        return lb
    elif lb == -1:
        return ub
    else:
        return ub if abs(arr[ub] - target) < abs(arr[lb] - target) else lb


def find_k_closest(arr: List[int], target: int, k: int) -> int:
    closest = find_closest(arr, target)
    counter = k - 1
    left, right = closest, closest + 1
    while counter >= 0 and left >= 0 and right + 1 <= len(arr) - 1:
        if abs(arr[left - 1] - target) < abs(arr[right + 1] - target):
            left -= 1
        else:
            right += 1
        counter -= 1
    for _ in range(counter - 1):
        if left >= 0:
            left -= 1
        else:
            right += 1
    return arr[left:(right+1)]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {100}, lower bound: {lower_bound(arr, 100)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, lower bound: {lower_bound(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, lower bound: {lower_bound(arr, 1)}")

    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {100}, upper bound: {upper_bound(arr, 100)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, upper bound: {upper_bound(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, upper bound: {upper_bound(arr, 1)}")

    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find leftmost: {find_leftmost(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, find leftmost: {find_leftmost(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find rightmost: {find_rightmost(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, find rightmost: {find_rightmost(arr, 0)}")

    arr = [1, 2, 100, 101, 102]
    target = 99
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = 200
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = 10
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = -1
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [2, 2, 2]
    target = 2
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 2, 2]
    target = 2
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 2, 2, 4, 4, 4]
    target = 3
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")

    arr = [1, 2, 100, 101, 102]
    target = 99
    k = 3
    import pdb
    pdb.set_trace()
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")
