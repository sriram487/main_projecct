import requests
from flask import Flask, render_template, request
from sqlalchemy import create_engine, select, text, insert
from sqlalchemy.orm import Session
from user import User
from datetime import datetime
import requests

app = Flask(__name__)

# defining database credentials
user = 'sriram'
password = 'root'
host = '127.0.0.1'
port = 3306
database = 'Bio-metric System'


def get_connection():
    return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))


engine = get_connection()
session = Session(engine)


@app.route('/update_db', methods=['GET', 'POST'])
def update_db():
    txt = request.data
    print(txt)
    date = str(datetime.now().date())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    temp = bool(session.query(User).filter_by(name=txt, date=date).first())

    if not temp:
        stmt = insert(User).values(id=id, name=txt, date=date, time=current_time)
        compiled = stmt.compile()

        session.execute(stmt)
        session.commit()

    return ""


@app.route('/', methods=['GET', 'POST'])
def index():
    lst = []
    if request.method == 'POST':
        date = request.form['date']
        stmt = select(User).where(User.date == date)
        result = session.execute(stmt)
        for data in result.scalars():
            lst.append(f"Name : {data.name} Id : {data.id} Date : {data.date} Time : {data.time}")
        if len(lst) == 0:
            return render_template("empty.html")

        return render_template("display.html", lst=lst)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
