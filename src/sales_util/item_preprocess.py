from typing import Optional
from sales_util.items import Item


def clean_item(item: Item,  seen_names: set) -> Optional[Item]:
    
    # Remove duplicates
    if item.name in seen_names:
        return None
    seen_names.add(item.name)

    # Remove invalid price
    if item.price is None or item.price < 0:
        return None
    
    # Remove extreme price outliers and zero dollar prices
    if item.price > 50 or item.price == 0:
        return None

    # Remove review games
    if (item.positive + item.negative) == 0:
        return None

    # Cap extreme values instead of removing
    item.peakCCU = min(item.peakCCU, 100_000)     
    item.dlcCount = min(item.dlcCount, 20)        
    item.positive = min(item.positive, 50_000)
    item.negative = min(item.negative, 10_000)

    item.price = round(item.price, 2)

    return item