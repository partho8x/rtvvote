from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.rtvonline.com",
    "Connection": "keep-alive",
    "Referer": "https://www.rtvonline.com/opinion-poll",
    "Cookie": "fpestid=aQIFLYXcZMiVMn9D-svrbbSVpOrlW0hZhVjxwO8rDLjSP3XL3AagD_ahfs3ugxIO0OWVag; _ga_Q7WC2NJ42X=GS1.1.1725005166.2.1.1725005624.0.0.0; _ga=GA1.1.2141067350.1724581903; __gads=ID=64c93c0fbaf02a31:T=1724581911:RT=1724581911:S=ALNI_Ma69HrSRZ2GD9tH0pYaz5EP1rZ83w; __gpi=UID=00000ed6fe64b8af:T=1724581911:RT=1724581911:S=ALNI_MbJ6TdoPLya4o-l-e83D9745Ham0w; __eoi=ID=2f7fcfef2dce03fb:T=1724581911:RT=1724581911:S=AA-AfjZYcgI_ybPhpUKrb127tlSo; _cc_id=5795eb759a143f5fbe586b8641d8f7d0; cto_bundle=IsBpbl91TWtiYktETjVYSWxtVkhMN2N1TE1ibGNrREg2JTJGZzJoT1pzUFBiZ1dRZWxoVGM5Nm0lMkIzdmpQdTl6RHFqZlJma2glMkZwMjB0bWVqbDhQcmo2eTlPNGRhbzBNRFJ1NU1VNnIlMkJ3RlZvT0kwNEFMWEhlRzM3a2NBQiUyQms3c0Z6cmQ1M0wlMkZzZmlKenZFZ3FFV2RhJTJGRkJyekdOQSUzRCUzRA; PHPSESSID=78e5f4de70d12602f4fc86572be64e18; panoramaId_expiry=1725091642923; lses=1.2VtDQHUDRgf0b9UgEz7uUMhzwFxBdrWA",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "TE": "trailers"
}

# Data for the POST request
data = {
    "poll_id": "83",
    "option_index": "1"
}

# URL of the endpoint
url = "https://www.rtvonline.com/templates/web-view/opinion_poll/ajax/vote_submit.php"

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    num_requests = int(request.form.get('num_requests', 10))  # Number of requests, default is 10
    results = []

    for _ in range(num_requests):
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            results.append("Vote submitted successfully.")
        else:
            results.append(f"Failed to submit vote. Status code: {response.status_code}")

    return jsonify(results=results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
