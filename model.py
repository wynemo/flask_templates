# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

from util import get_timestamp

Base = declarative_base()
metadata = Base.metadata


class TRph(Base):
    __tablename__ = 't_rph'

    id = Column(INTEGER(11), primary_key=True)
    PHONE = Column(String(255))
    NAME = Column(String(255))
    BOOKER_NAME = Column(String(255))
    COUNTRY_CODE = Column(String(255))
    PROPERTYCODE = Column(String(255))
    LOCATION = Column(String(255))
    NET_SPEND = Column(String(255))
    PLATFORM = Column(String(255))
    IP_ADDRESS = Column(String(255))
    LANG_CODE = Column(String(255))
    LOCAL_TIME_BOOKING_AT = Column(String(255))
    NATIONALITY = Column(String(255))
    BOOK_DATE = Column(String(255))
    NUMERICPHONE = Column(String(2048))
    CURRENCY_CODE = Column(String(255))
    LANG = Column(String(255))
    BIRTH = Column(String(255))
    CHECK_IN_DATE = Column(String(255))
    NIGHTS = Column(String(255))
    GROSS_SPEND = Column(String(255))
    LOYALTY_NO = Column(String(255))
    EMAIL = Column(String(255))
    CHECK_OUT_DATE = Column(String(255))
    HOTEL_NAME = Column(String(255))
    ROOM_NUMBER = Column(String(255))
    CANCEL_DATE = Column(String(255))
    longitude_latitude = Column(String(255))

    def to_dict(self):
        return dict(
            id=self.id,
            phone=self.PHONE,
            name=self.NAME,
            booker_name=self.BOOKER_NAME,
            country_code=self.COUNTRY_CODE,
            propertycode=self.PROPERTYCODE,
            location=self.LOCATION,
            net_spend=self.NET_SPEND,
            platform=self.PLATFORM,
            ip_address=self.IP_ADDRESS,
            lang_code=self.LANG_CODE,
            local_time_booking_at=get_timestamp(self.LOCAL_TIME_BOOKING_AT),
            nationality=self.NATIONALITY,
            book_date=get_timestamp(self.BOOK_DATE),
            numericphone=self.NUMERICPHONE,
            currency_code=self.CURRENCY_CODE,
            lang=self.LANG,
            birth=self.BIRTH,
            check_in_date=get_timestamp(self.CHECK_IN_DATE),
            nights=self.NIGHTS,
            gross_spend=self.GROSS_SPEND,
            loyalty_no=self.LOYALTY_NO,
            email=self.EMAIL,
            check_out_date=get_timestamp(self.CHECK_OUT_DATE),
            hotel_name=self.HOTEL_NAME,
            room_number=self.ROOM_NUMBER,
            cancel_date=get_timestamp(self.CANCEL_DATE),
            longitude_latitude=self.longitude_latitude
        )


class TRphIndex(Base):
    __tablename__ = 't_rph_index'

    id = Column(INTEGER(11), primary_key=True)
    PHONE = Column(String(255))
    NAME = Column(String(255))
    BOOKER_NAME = Column(String(255))
    COUNTRY_CODE = Column(String(255))
    PROPERTYCODE = Column(String(255))
    LOCATION = Column(String(255))
    NET_SPEND = Column(String(255))
    PLATFORM = Column(String(255))
    IP_ADDRESS = Column(String(255))
    LANG_CODE = Column(String(255))
    LOCAL_TIME_BOOKING_AT = Column(String(255))
    NATIONALITY = Column(String(255))
    BOOK_DATE = Column(String(255))
    NUMERICPHONE = Column(String(2048))
    CURRENCY_CODE = Column(String(255))
    LANG = Column(String(255))
    BIRTH = Column(String(255))
    CHECK_IN_DATE = Column(String(255))
    NIGHTS = Column(String(255))
    GROSS_SPEND = Column(String(255))
    LOYALTY_NO = Column(String(255))
    EMAIL = Column(String(255))
    CHECK_OUT_DATE = Column(String(255))
    HOTEL_NAME = Column(String(255))
    ROOM_NUMBER = Column(String(255))
    CANCEL_DATE = Column(String(255))
    longitude_latitude = Column(String(255))

    def to_dict(self):
        return dict(
            id=self.id,
            phone=self.PHONE,
            name=self.NAME,
            # booker_name=self.BOOKER_NAME,
            country_code=self.COUNTRY_CODE,
            id_num='',
            # propertycode=self.PROPERTYCODE,
            # location=self.LOCATION,
            # net_spend=self.NET_SPEND,
            # platform=self.PLATFORM,
            # ip_address=self.IP_ADDRESS,
            # lang_code=self.LANG_CODE,
            # local_time_booking_at=self.LOCAL_TIME_BOOKING_AT,
            # nationality=self.NATIONALITY,
            # book_date=self.BOOK_DATE,
            # numericphone=self.NUMERICPHONE,
            # currency_code=self.CURRENCY_CODE,
            # lang=self.LANG,
            birth=self.BIRTH,
            # check_in_date=self.CHECK_IN_DATE,
            # nights=self.NIGHTS,
            # gross_spend=self.GROSS_SPEND,
            # loyalty_no=self.LOYALTY_NO,
            email=self.EMAIL,
            # check_out_date=self.CHECK_OUT_DATE,
            # hotel_name=self.HOTEL_NAME,
            # room_number=self.ROOM_NUMBER,
            # cancel_date=self.CANCEL_DATE,
            # longitude_latitude=self.longitude_latitude
        )
