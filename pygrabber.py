from flask import Flask, render_template, request
from pymediathek import MediathekOptions, find_programme

import aiohttp

app = Flask(__name__)

session = aiohttp.ClientSession()

@app.route('/', methods=('GET', 'POST'))
async def index():
    if request.method == 'POST':
        url = request.form['url']
        programme = await find_programme(field='website_url', target_value=url, options=MediathekOptions(working_directory=".", http_session=session))
        if programme:
            return render_template('result.html', result=programme)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')