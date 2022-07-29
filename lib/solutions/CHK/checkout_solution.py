# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0

    total_price = 0

    for shop_item in skus:
        if shop_item not in ["A", "B", "C", "D", "E"] or shop_item == "":
            total_price = -1
            return -1

    for item in skus:
        if item == "A":
            total_price += 50
            a_count += 1

        if item == "C":
            total_price += 20
            c_count += 1
        if item == "D":
            total_price += 15
            d_count += 1
        if item == "E":
            total_price += 40
            e_count += 1

        if item == "B":
            b_count += 1
            b_count = e_count_check(e_count, b_count)
            total_price += 30

    if a_count == 10:
        total_price -= 100
    elif a_count == 9:
        total_price -= 70
    elif a_count == 8:
        total_price -= 70
    elif a_count == 7:
        total_price -= 50
    elif a_count == 6:
        total_price -= 50
    elif a_count == 5:
        total_price -= 50
    elif a_count >= 3 <= 4:
        total_price -= 20

    if e_count == 6:
        b_count -= 3
    elif e_count == 5:
        b_count -= 2
    elif e_count == 4:
        b_count -= 2
    elif e_count == 3:
        b_count -= 1
    elif e_count == 2:
        b_count -= 1

    if b_count >= 2 <= 3:
        total_price -= 15
    if b_count >= 4 <= 5:
        total_price -= 15

    return total_price


def e_count_check(e_count, b_count):
    if e_count == 6:
        b_count -= 3
    elif e_count == 5:
        b_count -= 2
    elif e_count == 4:
        b_count -= 2
    elif e_count == 3:
        b_count -= 1
    elif e_count == 2:
        b_count -= 1

    return b_count

