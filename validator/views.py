from django.http import JsonResponse, HttpResponse
from .constants import VALIDATOR_URL, REFERER_URL
from database.views import kickoff_database_tasks
import requests
import cfscrape

query_params_for_detailed_search = '?truncateResponse=false'
def get_response(email):
    """
    Verifies email with the designated 3rd party server.

    :param email: str
    :return: request object
    """
    session = requests.session()
    headers = {
        'user-agent': 'Mozilla/5.0',
        'accept-language': 'en-GB',
        'referrer': REFERER_URL,
        'hibp-api-key': '578054d5464941519b4a65ccb664c3e6',
        'Content-Type': 'application/json',
    }
    scraper = cfscrape.create_scraper(sess=session)
    response = scraper.get(url=VALIDATOR_URL + email + query_params_for_detailed_search, headers=headers)
    kickoff_database_tasks(email=email, res=response)
    return response
    # curl 'https://haveibeenpwned.com/unifiedsearch/sonicxxx7@gmail.com' -H 'user-agent: Mozilla/5.0' -H 'accept-language: en-GB' -H 'rerferrer: https://www.haveibeenpwned.com'


def check_if_email_hacked(request, email):
    """
    Parse the request and send proper response back.

    :param request: request object
    :param email: str
    :return: response object
    """
    response = get_response(email)
    if response.status_code == 404:
        return JsonResponse({
            'status': 'safe',
            'breaches': 0
        }, status=404)

    elif response.status_code == 200:
        kickoff_database_tasks(email, response)
        return HttpResponse(response)

    else:
        return JsonResponse({
            'status': 'failed',
            'message': 'API request was not proper'
        }, status=response.status_code)
