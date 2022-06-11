from email import header
import json
import requests

from AcmeSupport.settings import ZENDESK_EMAIL, ZENDESK_PASSWORD,ZENDESK_TICKET_DOMAIN

def list_ticket():
    data=requests.get(ZENDESK_TICKET_DOMAIN,auth=(ZENDESK_EMAIL,ZENDESK_PASSWORD))
    return data.json()

def ticket_create(data):
    data={
        'ticket':data
    }
    header={"Content-Type": "application/json"}
    data=requests.post(ZENDESK_TICKET_DOMAIN,auth=(ZENDESK_EMAIL,ZENDESK_PASSWORD),headers=header,data=json.dumps(data))

def create_user(data):
    data = {
        'user': data
    }