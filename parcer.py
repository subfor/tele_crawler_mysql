import os
from urllib.parse import urlparse, parse_qs
import requests

DOMAIN = os.getenv('DOMAIN')


def get_data(page_url: str):
    parsed = urlparse(page_url)
    try:
        captured_value = parse_qs(parsed.query)['id_auc'][0]
        url = f"https://{DOMAIN}/public/PublicHandler.ashx?CommandName=jResults&id_auc={captured_value}&info=Y&lan=ua&fl_FullNumber=&fl_Direction=&fl_Owner=&fl_Goods=&empty_filter=Y"
        response = requests.get(url, timeout=(1, 1))
        val = response.json()
        date = val['info']['TradeDate']
        # r_data = [{
        #     "date": date,
        #     "position": row['Number'],
        #     "data": {
        #         "seller": row['OwnerName'],
        #         "goods": row['Goods'],
        #         "kind": row['GoodsComment'],
        #         "delivery basis ": row['Base_point'],
        #         "place": row['DeliveryPlace'],
        #         "transport": row['Delivery_type'],
        #         "lot count": row['AgreeCount'],
        #         "value": row['ResultFullSize'],
        #         "min price": row['MinPrice'],
        #         "max price": row['MaxPrice'],
        #         "average price": row['AvgPrice']
        #
        #     }
        # } for row in val['rows']]
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
    except KeyError:
        print("incorrect id")
    return r_data


if __name__ == '__main__':
    pass
