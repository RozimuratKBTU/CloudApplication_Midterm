from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

# Локальное хранилище встреч
meetings = []


NOTIFY_FUNCTION_URL = "https://us-central1-polar-ray-475006-i4.cloudfunctions.net/greet_user"


def send_notification(title, date, time, description):
    data = {
        "title": title,
        "date": date,
        "time": time,
        "description": description
    }
    try:
        requests.post(NOTIFY_FUNCTION_URL, json=data)
    except Exception as e:
        print(f"Ошибка при отправке уведомления: {e}")


@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        time = request.form['time']
        description = request.form['description']

        meetings.append({
            "title": title,
            "date": date,
            "time": time,
            "description": description,
            "created_at": datetime.now()
        })

        send_notification(title, date, time, description)
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(meetings):
        meetings.pop(index)
    return redirect(url_for('index'))


@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.json
    resp = requests.post(NOTIFY_FUNCTION_URL, json=data)
    return jsonify(resp.json()), resp.status_code

# @app.route('/test-error')
# def test_error():
#     # Это искусственная ошибка для проверки мониторинга
#     raise Exception("This is a test 500 error for monitoring check!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)





