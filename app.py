import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common import dao

from flask import Flask, render_template, request
import pandas as pd 

app = Flask(__name__, static_url_path='/static')
DAO = dao.DAO()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/class/0')
def show_class_0_students():
    attendance = DAO.get_all_student_in_class(0)
    df = pd.DataFrame(attendance, columns=['학생 id', '확인 시간'])
    return df.to_html()

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
    app.run(debug=True, threaded=True)