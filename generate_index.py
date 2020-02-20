import os
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from model import TRph, TRphIndex


app = Flask(__name__)

mysqlurl = 'mysql+pymysql://sonar:sonar&404@192.168.56.103:3306/sonar_dev?charset=utf8mb4'
config = dict(
    SQLALCHEMY_DATABASE_URI=mysqlurl,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
    SQLALCHEMY_POOL_SIZE=100,
    SQLALCHEMY_MAX_OVERFLOW=200,
    SQLALCHEMY_POOL_RECYCLE=7200,
    SQLALCHEMY_ECHO=True if os.environ.get('ECHO') else False,
)

app.config.update(**config)

db = SQLAlchemy()
db.init_app(app)


all_phone_name = set()
with app.app_context():
    for each in db.session.query(TRph).all():
        key = (each.PHONE, each.NAME, each.BOOKER_NAME)
        if key not in all_phone_name:
            all_phone_name.add(key)
            index = TRphIndex(PHONE=each.PHONE, NAME=each.NAME, BOOKER_NAME=each.BOOKER_NAME,
                      COUNTRY_CODE=each.COUNTRY_CODE,
                      PROPERTYCODE=each.PROPERTYCODE,
                      LOCATION=each.LOCATION,
                      NET_SPEND=each.NET_SPEND,
                      PLATFORM=each.PLATFORM,
                      IP_ADDRESS=each.IP_ADDRESS,
                      LANG_CODE=each.LANG_CODE,
                      LOCAL_TIME_BOOKING_AT=each.LOCAL_TIME_BOOKING_AT,
                      NATIONALITY=each.NATIONALITY,
                      BOOK_DATE=each.BOOK_DATE,
                      NUMERICPHONE=each.NUMERICPHONE,
                      CURRENCY_CODE=each.CURRENCY_CODE,
                      LANG=each.LANG,
                      BIRTH=each.BIRTH,
                      CHECK_IN_DATE=each.CHECK_IN_DATE,
                      NIGHTS=each.NIGHTS,
                      GROSS_SPEND=each.GROSS_SPEND,
                      LOYALTY_NO=each.LOYALTY_NO,
                      EMAIL=each.EMAIL,
                      CHECK_OUT_DATE=each.CHECK_OUT_DATE,
                      HOTEL_NAME=each.HOTEL_NAME,
                      ROOM_NUMBER=each.ROOM_NUMBER,
                      CANCEL_DATE=each.CANCEL_DATE,
                      longitude_latitude=each.longitude_latitude,
                      )
            db.session.add(index)
    db.session.commit()
    print('here')
