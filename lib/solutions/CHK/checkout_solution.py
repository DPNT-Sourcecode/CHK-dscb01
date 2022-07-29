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

            a_count = a_count * 50
            print("A count == {}".format(a_count))
            b_count = b_count * 30
            print("B count == {}".format(b_count))
            c_count = c_count * 20
            print("C count == {}".format(c_count))
            d_count = d_count * 15
            print("D count == {}".format(d_count))

            total_price = a_count + b_count + c_count + d_count

            if a_count == 3:
                total_price = total_price - 20

            if b_count == 3:
                total_price = total_price - 15

    return total_price




