import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))


def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


import requests
from .models import DealerReview

def get_dealer_reviews_from_cf(dealer_id):
    url = f"https://05398821-f96a-4e1d-adc4-02249a5fb467-bluemix.cloudant.com/dashboard.html#database/reviews/_all_docs"
    response = requests.get(url)
    reviews_data = response.json()
    reviews = []
    for review_data in reviews_data:
        review = DealerReview(
            dealership=review_data["dealership"],
            name=review_data["name"],
            purchase=review_data["purchase"],
            review=review_data["review"],
            purchase_date=review_data["purchase_date"],
            car_make=review_data["car_make"],
            car_model=review_data["car_model"],
            car_year=review_data["car_year"],
            sentiment=review_data["sentiment"],
            id=review_data["id"]
        )
        reviews.append(review)
    return reviews


 if api_key:
   # Basic authentication GET
   request.get(url, params=params, auth=, ...)
 else:
   # no authentication GET
   request.get(url, params=params)

...
  params = dict()
  params["text"] = kwargs["text"]
  params["version"] = kwargs["version"]
  params["features"] = kwargs["features"]
  params["return_analyzed_text"] = kwargs["return_analyzed_text"]
  response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
...
...
review_obj.sentiment = analyze_review_sentiments(review_obj.review)

import requests

def post_request(url, json_payload, **kwargs):
    response = requests.post(url, json=json_payload, **kwargs)
    return response.json()


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



