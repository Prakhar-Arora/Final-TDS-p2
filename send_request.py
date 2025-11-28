# /// script
# dependencies = [
#   "requests"
# ]
# ///

import requests

payload={
  "email": "22f3000671@ds.study.iitm.ac.in",
  "secret": "AVerySecretKey",
  "url": "https://tds-llm-analysis.s-anand.net/demo"
}

r = requests.post("http://localhost:8000/task",json=payload)

print(r.json())
# https://tds-llm-analysis.s-anand.net/demo-scrape?email=22f3000671%40ds.study.iitm.ac.in&id=21516
# https://tds-llm-analysis.s-anand.net/demo-audio?email=22f3000671%40ds.study.iitm.ac.in&id=16884