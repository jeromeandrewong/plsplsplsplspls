"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


"""


def totalFruit(fruits) -> int:
    """
    :type fruits: List[int]
    :rtype: int
    """

    # using sliding window (variable length) algo because we are dealing with checking combinations of subarrays.
    # when to expand window: when its a valid subarray (<3 distinct types of fruit)
    # when to contract window: when invalid subarray
    # stop when at the end of the array

    # start of window
    start = 0
    # track fruits in current window
    state = {}
    # track max fruits possible throughout the loop
    max_fruits = 0

    for end in range(len(fruits)):
        # update current state, key is a fruit and val is the count
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        while len(state) > 2:
            # when we reach a invalid subarray, remove first fruit count, if count reaches 0, remove item from state, contract sliding window
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start += 1

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits


def test_totalFruit():
    # Test case with fruits [3,3,2,1,2,1,0]
    # Expected output: 4 (can pick [2,1,2,1])
    fruits = [3, 3, 2, 1, 2, 1, 0]
    assert totalFruit(fruits) == 4, f"Expected 4 but got {totalFruit(fruits)}"
    print("All test cases passed!")


test_totalFruit()
