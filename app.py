from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    url = 'https://natesnewsletter.substack.com/feed'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
        return Response(r.content.decode('utf-8', errors='replace'), status=r.status_code, content_type='application/xml; charset=utf-8')
    except Exception as e:
        return Response(f'Error fetching feed: {e}', status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

