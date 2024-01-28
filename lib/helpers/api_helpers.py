from bs4 import BeautifulSoup
import pdb
import re

def generate_user_payload(new_user):
    user_payload = {
        "customer.firstName": new_user.firstname,
        "customer.lastName": new_user.lastname,
        "customer.address.street": new_user.address,
        "customer.address.city": new_user.city,
        "customer.address.state": new_user.state,
        "customer.address.zipCode": new_user.zip_code,
        "customer.phoneNumber": new_user.phone_number,
        "customer.ssn": new_user.ssn,
        "customer.username": new_user.username,
        "customer.password": new_user.password,
        "repeatedPassword": new_user.password,
    }
    return user_payload


def extract_customer_id_from_html(response_body):
    parsed_body = BeautifulSoup(response_body, 'html.parser')
    script_tag = parsed_body.find('script', text=re.compile('services_proxy/bank/customers/'))
    script_content = script_tag.text if script_tag else None
    if script_content:
        # Use regular expression to extract the customer ID
        match_data = re.search(r'(\d+) \+ "/accounts"', script_content)
        if match_data:
            return match_data.group(1)

    return None