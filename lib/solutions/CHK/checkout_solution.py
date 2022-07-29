# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0

    total_price = 0

    for shop_item in skus:
        if shop_item not in ["A", "B", "C", "D"] or shop_item == "":
            total_price = -1
            break
        else:
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

            if a_count >= 3:
                total_price -= 20
            if b_count >= 2:
                total_price -= 15

    return total_price
