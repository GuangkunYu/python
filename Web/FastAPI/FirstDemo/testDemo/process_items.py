from typing import List, Set, Tuple, Dict


# 定义一个由str组成的list变量
def process_items(items: List[str]):
    for item in items:
        print(item)


def process_items(items_t: Tuple[int, int, int], items_s: Set[bytes]):
    return items_t, items_s


def process_items(prices:Dict[str, float]):
    for item_name,item_price in prices.items():
        print(item_name)
        print(item_price)
