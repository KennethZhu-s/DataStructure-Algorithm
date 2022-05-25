goods = [(60, 10), (120, 30), (100, 20)]      # (price, weight)
goods.sort(key=lambda x: x[0]/x[1], reverse=True)

def fractional_backpack(goods, w):
    print("goods:", goods)
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
        else:
             m[i] = w / weight
             total_v += m[i] * price
             w = 0
             break
    return total_v, m

print(fractional_backpack(goods, 50))
