import os
import asyncio
from urllib.parse import urlparse, parse_qs
import aiohttp

DOMAIN = os.getenv('DOMAIN')


async def get_data(page_url: str):
    parsed = urlparse(page_url)
    try:
        captured_value = parse_qs(parsed.query)['id_auc'][0]
        url = f"https://{DOMAIN}/public/PublicHandler.ashx?CommandName=jResults&id_auc={captured_value}&info=Y&lan=ua&fl_FullNumber=&fl_Direction=&fl_Owner=&fl_Goods=&empty_filter=Y"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                val = await response.json()
        date = val['info']['TradeDate']
        r_data = [{
            "date": date,
            "position": row['Number'],
            "seller": row['OwnerName'],
            "goods": row['Goods'],
            "kind": row['GoodsComment'],
            "delivery_basis ": row['Base_point'],
            "place": row['DeliveryPlace'],
            "transport": row['Delivery_type'],
            "lot_count": row['AgreeCount'],
            "value": row['ResultFullSize'],
            "min_price": row['MinPrice'],
            "max_price": row['MaxPrice'],
            "average_price": row['AvgPrice']
        } for row in val['rows']]
        return r_data
    except KeyError:
        print("incorrect id")


if __name__ == '__main__':
    pass
