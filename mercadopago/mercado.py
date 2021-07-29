import mercadopago
import json

mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

def index(req, **kwargs):
        preferenceResult = mp.get_preference("PREFERENCE_ID")

        return json.dumps(preferenceResult, indent=4) 

def index(req, **kwargs):
        preference = {
            "items": [
                {
                    "title": "Test",
                    "quantity": 1,
                    "currency_id": "USD",
                    "unit_price": 10.4
                }
            ]
        }

        preferenceResult = mp.create_preference(preference)

        return json.dumps(preferenceResult, indent=4)         


def index(req, **kwargs):
        preference = {
                "items": [
                    {
                        "title": "Test Modified",
                        "quantity": 1,
                        "currency_id": "USD",
                        "unit_price": 20.4
                    }
                ]
            }

        preferenceResult = mp.update_preference(id, preference)

        return json.dumps(preferenceResult, indent=4)          


def index(req, **kwargs):
        filters = {
            "id": None,
            "external_reference": None
        }

        searchResult = mp.search_payment(filters)

        return json.dumps(searchResult, indent=4)

import mercadopago
import json

def index(req, **kwargs):
        mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
        paymentInfo = mp.get_payment (kwargs["id"])

        if paymentInfo["status"] == 200:
            return json.dumps(paymentInfo, indent=4)
        else:
            return None   

def index(req, **kwargs):
        result = mp.cancel_payment("ID")
        // Show result
return json.dumps(result, indent=4)


def index(req, **kwargs):
        result = mp.refund_payment("ID")

        // Show result
        return json.dumps(result, indent=4)



