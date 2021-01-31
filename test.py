# def remove_token_from_list(the_list=["a", "a", "b", "b", "c", "c"], token="b"):
#     """
#
#     Parameters
#     ----------
#     the_list
#     token
#
#     Returns
#     -------
#
#     """
#     if token not in the_list:
#         return the_list
#     else:
#         the_list.remove(token)
#         return remove_token_from_list(the_list, token)
#
#
# def remove_token_from_list(the_list=["a", "a", "b", "b", "c", "c"], token="b"):
#     """
#
#     Parameters
#     ----------
#     the_list
#     token
#
#     Returns
#     -------
#
#     """
#     if token not in the_list:
#         return the_list
#     else:
#         the_list.remove(token)
#         return remove_token_from_list(the_list, token)
#
#
# print(remove_token_from_list())
#
# list_ = ["s", "s", "w", "w", "c", "b", "d"]
#
#
# print(list_)


def remove(list1, token1=5):
    print(f"list1: {list1}")
    print(f"token1: {token1}")
    while token1 in list1:
        list1.remove(token1)
    return list1


a = [2, 4, 5, 5, 6]
t = 5
r = remove(a)
print(r)

