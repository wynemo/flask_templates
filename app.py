import datetime
import os
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from model import TRph, TRphIndex
from util import get_timestamp

app = Flask(__name__)

# mysqlurl = 'mysql+pymysql://sonar:sonar&404@192.168.56.103:3306/sonar_dev?charset=utf8mb4'
mysqlurl = 'sqlite:///1.db'
config = dict(
    SQLALCHEMY_DATABASE_URI=mysqlurl,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
    # SQLALCHEMY_POOL_SIZE=100,
    # SQLALCHEMY_MAX_OVERFLOW=200,
    SQLALCHEMY_POOL_RECYCLE=280, # 280 seconds, if mysql idle is longer you can set it to 7200s
    SQLALCHEMY_ECHO=True if os.environ.get('ECHO') else False,
)

app.config.update(**config)

db = SQLAlchemy()
db.init_app(app)


@app.route('/detail',  methods=['GET'])
def detail():
    data = request.args
    _id = data.get('id', 1, int)

    query = db.session.query(TRphIndex).filter_by(id=_id)
    result = query.first()
    if not result:
        return '{}'

    query = db.session.query(TRph).filter_by(NAME=result.NAME, PHONE=result.PHONE, BOOKER_NAME=result.BOOKER_NAME)
    results = [each.to_dict() for each in query.all()]
    rv = {}
    rv['info'] = {
        'name': result.NAME,
        'phone': result.PHONE,
        'booker_name': result.BOOKER_NAME,
        'id_num': '',
        'birth': result.BIRTH,
        'email': result.EMAIL,
    }
    rv['records'] = results
    rv = json.dumps(rv)
    return rv



@app.route('/location',  methods=['GET'])
def location():
    data = request.args
    _id = data.get('id', 1, int)

    query = db.session.query(TRphIndex).filter_by(id=_id)
    result = query.first()
    if not result:
        return '{}'

    query = db.session.query(TRph).filter_by(NAME=result.NAME, PHONE=result.PHONE, BOOKER_NAME=result.BOOKER_NAME)
    results = [each.to_dict() for each in query.all()]
    rv = []
    for each in results:
        value = {}
        out_date = each['check_out_date']
        value['end_time'] = out_date
        in_date = each['check_in_date']
        if not in_date:
            value['time'] = value['end_time'] - int(each['nights']) * 3600 * 1000
        else:
            value['time'] = in_date
        import re
        obj = re.search(r'(-?\d+\.\d+),\s*(-?\d+\.\d+)', each['longitude_latitude']) #'14.633690, 121.040657'
        if not obj:
            continue
        value['coordinates'] = [obj.group(1), obj.group(2)]
        value['hotel_name'] = each['hotel_name']
        value['room_number'] = each['room_number']
        rv.append(value)
    rv = json.dumps(rv)
    return rv


@app.route('/',  methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_data(cache=False)
    else:
        data = request.args
    try:
        if isinstance(data, (str, bytes)):
            data = json.loads(data)
    except:
        data = {}
    new_data = {}
    for each in data:
        if each == 'longitude_latitude' or each == 'id':
            new_data[each] = data[each]
        elif each in ('pg', 'pg_size'):
            continue
        else:
            new_data[each.upper()] = data[each]

    pg = int(data.get('pg', 1))
    pg_size = int(data.get('pg_size', 20))
    offset = (pg - 1) * pg_size
    query = db.session.query(TRphIndex)
    if 'NAME' in new_data:
        query = query.filter(TRphIndex.NAME.ilike('%' + new_data['NAME'] + '%'))
        new_data.pop('NAME')
    query = query.filter_by(**new_data)
    total = query.count()
    results = [each.to_dict() for each in query.offset(offset).limit(pg_size).all()]
    rv = {}
    rv['size'] = len(results)
    rv['data'] = results
    rv['total'] = total
    rv = json.dumps(rv)
    return rv
