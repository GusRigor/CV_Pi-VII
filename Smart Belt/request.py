import requests

class request:
    def __init__(self, productCondition = "OK"):
        self.url = "https://smart-b-api.ue.r.appspot.com/api/v1/product/register"
        self.productType = "BANANA"
        self.productCondition = productCondition

    def post(self, quantity):
        r = requests.post(self.url, json = {
            "user": "3d729ae8-ad34-46ab-842b-e01e0785137c",
            "productType": self.productType,
            "quantity": quantity,
            "productCondition": self.productCondition
        }
        )
