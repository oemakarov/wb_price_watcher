
import requests
from lib.model import CardRequestModel

# https://card.wb.ru/cards/detail?nm=117647686;117647687;117647690;117647685;117647689;117647688


class WB():
    """docstring for WB."""

    BASE_URL = 'https://card.wb.ru/cards/detail?curr=rub&nm=' 

    def __init__(self):
        pass
    

    def get_products_data(self, ids: list[int]):
        return self.get_full_products_response_data(ids).data.products
        

    def get_full_products_response_data(self, ids: list[int]):
        resp = requests.get(self._compose_url(ids))
        return CardRequestModel.parse_raw(resp.text)
        
    
    def _compose_url(self, ids: list[int]):
        return self.BASE_URL + ';'.join([str(i) for i in ids])