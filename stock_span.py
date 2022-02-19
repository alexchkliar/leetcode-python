# can do O(n) with stack
def get_max_profit(array_of_product_prices):
    period = total_range = []
    total_range.append(1)
    period.append(0)

    for time_period in range(1, len(array_of_product_prices)):

        while len(period) > 0 and array_of_product_prices[time_period] >= array_of_product_prices[period[-1]]:
            period.pop()

        if len(period) > 0:
            total_range.append(time_period - period[-1])

        else:
            total_range.append(time_period + 1)

        period.append(time_period)

    return 1 + max(total_range)

array_of_product_prices = [11, 12, 11, 10 , 7, 13, 15]
print(get_max_profit(array_of_product_prices))
array_of_product_prices = [10, 9, 8, 7]
print(get_max_profit(array_of_product_prices))
