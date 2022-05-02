# def possible_permutations(elements):
#     if len(elements) <= 1:
#         yield elements
#     else:
#         for perm in possible_permutations(elements[1:]):
#             for i in range(len(elements)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + elements[0:1] + perm[i:]
#
#
# [print(n) for n in possible_permutations([1, 2, 3])]

from itertools import permutations
def possible_permutations(elements):
    res = permutations(elements)

    for r in res:
        yield list(r)


