import datetime


def get_timestamp(out_date):
    if not out_date:
        return None
    try:
        if len(out_date) <= 10:
            # datetime.datetime.strptime('4/13/2019', '%m/%d/%Y')
            date_obj = datetime.datetime.strptime(out_date, '%m/%d/%Y')
        else:
            try:
                # datetime.datetime.strptime('2013-08-17 00:00:00.0', '%Y-%m-%d %H:%M:%S.0')
                date_obj = datetime.datetime.strptime(out_date, '%Y-%m-%d %H:%M:%S.0')
            except:
                # 2/10/2018 20:12:59
                date_obj = datetime.datetime.strptime(out_date, '%m/%d/%Y %H:%M:%S')
        date_obj = date_obj.timestamp() * 1000
        return int(date_obj)
    except:
        return None
