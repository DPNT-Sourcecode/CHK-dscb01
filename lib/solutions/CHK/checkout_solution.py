# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0

    total_price = 0

    for shop_item in skus:
        if shop_item not in ["A", "B", "C", "D"]:
            return -1
        else:
            for item in skus:
                if item == "A":
                    a_count += 1
                if item == "B":
                    b_count += 1
                if item == "C":
                    c_count += 1
                if item == "D":
                    d_count += 1

            total_price = sum([a_count * 50, b_count * 30, c_count * 20, d_count * 15])

            if a_count > 3:
                total_price = - 20
            if b_count > 3:
                total_price = - 15

    return total_price



