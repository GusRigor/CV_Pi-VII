import requests

class request:
    def __init__(self, productCondition = "OK"):
        self.url = "https://smart-b-api.ue.r.appspot.com/"
        self.productType = "BANANA"
        self.productCondition = productCondition

    def post(self, quantity):
        data = {
            "userId": "17948f0c-9eb3-40b5-923e-28a5a346dadd",
            "productType": self.productType,
            "quantity": quantity,
            "productCondition": self.productCondition
        }
        requests.post(self.url, data=data)

