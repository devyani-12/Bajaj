import http.client
import json

conn = http.client.HTTPSConnection("customer-analytics-34146.my.salesforce-sites.com")
payload = json.dumps({
  "company": "BAJAJFINSV",
  "currentPrice": 1576,
  "accountNumber": "BFHL0018671",
  "githubRepoLink": " https://github.com/devyani-12/Bajaj/"
})
headers = {
  'bfhl-auth': '2110992497',
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=EqvFWOUIEe6OF9Vmbon52Q; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}
conn.request("POST", "/services/apexrest/buyStocks", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
