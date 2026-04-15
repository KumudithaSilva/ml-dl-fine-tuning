from typing import Optional
from sales_util.items import Item


def clean_item(item: Item) -> Optional[Item]:
    
    # Remove invalid price
    if item.price is None or item.price < 0:
        return None
    
    # Remove extreme price outliers
    if item.price > 2:
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