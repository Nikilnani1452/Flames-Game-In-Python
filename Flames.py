 def remove_common_chars(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                return [list1 + ["*"] + list2, True]
    return [list1 + ["*"] + list2, False]
if __name__ == "__main__":
    p1 = input("Player 1 name : ").lower().replace(" ", "")
    p1_list = list(p1)
    p2 = input("Player 2 name : ").lower().replace(" ", "")
    p2_list = list(p2)
    while True:
        ret_list = remove_common_chars(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        if not proceed:
            break
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    relationship_status = result[(count - 1) % len(result)]
    print("Relationship status:", relationship_status)