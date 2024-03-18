import requests
import json

url = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount"

payload = json.dumps({
  "name": "Devyani",
  "email": "devyani2497.be21@chitkara.edu.in",
  "rollNumber": 2110992497,
  "phone": 7018360227
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=EqvFWOUIEe6OF9Vmbon52Q; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
