import requests
from datetime import date, datetime
import sys
import json

def get_todays_funding_announcements(key, num):
    headers = {
        'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    
    timestamp = int(datetime.combine(date.today(), datetime.min.time()).timestamp())
    querystring = {"updated_since": timestamp}
    
    url_cb_funding = "https://crunchbase-crunchbase-v1.p.rapidapi.com/funding-rounds"

    response = requests.request("GET", url_cb_funding, headers=headers, params=querystring)
    funding_rounds = [x.get("properties") for x in response.json().get("data").get("items")]
    
    funding_uids = [ x.get("permalink") for x in funding_rounds if x.get("funding_type") == "seed" ]

    url_cb_details = [ url_cb_funding + "/{}".format(x) for x in funding_uids ]

    funded_companies = []
    for url_ in url_cb_details[:num]:
        company_response = requests.request("GET", url_, headers=headers).json()
        r = company_response.get("data").get("relationships")
        o = r.get("funded_organization").get("item").get("properties")
        funded_companies.append(o)

    return [ {
        "website": x.get("homepage_url"), 
        "description": x.get("description") 
    } for x in funded_companies ]

def get_company_lookalikes(funded_company_details, key):
    headers = {
        'x-rapidapi-host': "market-intelligence-by-automata.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    url_automata_similar = "https://market-intelligence-by-automata.p.rapidapi.com/similar"
    query_strings = [{"page":"0","link":x.get("website")} for x in funded_company_details]
    company_lookalikes = []
    for s in query_strings:
        response = requests.request("GET", url_automata_similar, headers=headers, params=s)
        company_lookalikes.append({
            "input_company": s.get("link"),
            "similar_companies": response.json().get("companies")
        })
    return company_lookalikes

def main(argv):
    if '-k' in sys.argv:
        key_index = [x for x in range(len(sys.argv)) if sys.argv[x] == "-k"][0]
        if len(sys.argv) >= key_index + 2:
            rapid_api_key = sys.argv[key_index + 1]
        else:
            print("no rapid api key")
            sys.exit(2)
    if '-max' in sys.argv:
        max_index = [x for x in range(len(sys.argv)) if sys.argv[x] == "-max"][0]
        if len(sys.argv) >= max_index + 2:
            max_num = int(sys.argv[max_index + 1])
        else:
           max_num = 5
    else:
        max_num = 5
   
    funding_recipients = get_todays_funding_announcements(rapid_api_key, max_num)
    company_lookalikes = get_company_lookalikes(funding_recipients, rapid_api_key)
    with open('company_lookalikes_{}.json'.format(int(datetime.now().timestamp())), 'w') as outfile:
        json.dump(company_lookalikes, outfile)
    print("Done!")

if __name__ == "__main__":
    main(sys.argv[1:])
    



