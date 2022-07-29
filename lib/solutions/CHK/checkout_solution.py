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
        if item == "B":
            total_price += 30
            b_count += 1
        if item == "C":
            total_price += 20
            c_count += 1
        if item == "D":
            total_price += 15
            d_count += 1
        if item == "E":
            total_price += 40
            e_count += 1

    if a_count == 10:
        total_price -= 100
    elif a_count == 9:
        total_price -= 70
    elif a_count == 8:
        total_price -= 70
    elif a_count == 6:
        total_price -= 50
    elif a_count == 5:
        total_price -= 50
    elif a_count >= 3 <= 4:
        total_price -= 20

    if b_count >= 2 <= 3:
        total_price -= 15
    if b_count >= 4 <= 5:
        total_price -= 15

    if e_count >= 2 <= 3:
        total_price -= 30
    if e_count >= 4 <= 5:
        total_price -= 30

    return total_price


