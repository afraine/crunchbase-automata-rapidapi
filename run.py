import requests
from datetime import date, datetime

def setup_headers(rapid_api_key):
    headers_cb = {
        'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': rapid_api_key
    }
    headers_automata = {
        'x-rapidapi-host': "market-intelligence-by-automata.p.rapidapi.com",
        'x-rapidapi-key': rapid_api_key
    }
    return (headers_cb, headers_automata)

def get_todays_funding_announcements():
    querystring = {"updated_since": timestamp}
    url_cb_funding = "https://crunchbase-crunchbase-v1.p.rapidapi.com/funding-rounds"

    funding_response = requests.request("GET", url_cb_funding, headers=headers_cb, params=querystring)
    funding_rounds = funding_response.get("data").get("items")
    funding_round_uuid = [x.get("properties").get("permalink") for x in funding_rounds]

    return funding_round_uuid

def get_funding_recipients(funding_uuids):
    url_cb_details = ["https://crunchbase-crunchbase-v1.p.rapidapi.com/funding-rounds/{}".format(x) for x in funding_uuids]

    funded_companies = []
    for url_ in url_details:
        company_response = requests.request("GET", url_cb_details, headers=headers_cb)
        funded_companies.push(company_response.get("data").get("relationships").get("funded_organizations").get("item").get("properties")

    funded_company_details = [{"website": x.get("website"), "description": x.get("description") } for x in funded_companies]

    return funded_company_details

def get_similar_companies_with_website(company_details):
    url_automata_similar = "https://market-intelligence-by-automata.p.rapidapi.com/similar"
    query_strings = [{"page":"0","link":x.get("website")} for x in funded_company_details]
    similar_companies = []
    for s in query_strings:
        similar_companies_response = requests.request("GET", url_automata_similar, headers=headers_automata, params=s)
        similar_companies.push({
            "input_company": s.get("link"),
            "similar_companies": similar_companies_response.get("companies")
        })
    return similar_companies





