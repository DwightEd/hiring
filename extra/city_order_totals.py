"""按城市汇总订单金额。

来源主题：京东算法岗 https://www.nowcoder.com/discuss/931679472032444416
原帖只提供主题。本仓库练习约定：输入 (城市, 金额整数分)，输出城市→总分。
允许负数表示退款，不去重；若要按订单 ID 去重，必须另外给出覆盖/累加规则。
使用整数金额避免浮点累计误差。时间 O(n) 期望，空间 O(c)。
"""


def city_order_totals(orders):
    totals = {}
    for city, cents in orders:
        if not isinstance(cents, int) or isinstance(cents, bool):
            raise ValueError("金额必须是整数分")
        totals[city] = totals.get(city, 0) + cents
    return totals
