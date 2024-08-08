from flask import Flask
from flask import render_template, request
import re
from collections import Counter

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files['file'].read()  # получаем битовый вид файла
        txt = str(f.decode('utf-8'))  # Чтобы получить строковый вид из файла

        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips = re.findall(pattern, txt)
        result = Counter(ips).most_common(10)  # список кортежей из двух элементов

        ban = []
        for key, value in result:
            if value > 100:
                ban.append({'ip': key,
                            'frequency': value})

        return render_template('index.html', ips=ban)

    return render_template('index.html')


@app.route('/users', methods=['POST', 'GET'])
def create_users():
    username = request.form.get('user')
    print(username)
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
