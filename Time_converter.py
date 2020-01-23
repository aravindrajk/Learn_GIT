from datetime import datetime
from pytz import timezone
from datetime import timedelta

# Input format can be in any of the format in fmt variable. Enable the correct one accordingly
#fmt = "%m/%d/%Y %I:%M:%S %p"
fmt = "%m/%d/%Y %H:%M:%S"
#fmt = "%m/%d/%Y %H:%M"
#fmt = "%Y/%m/%d %H:%M:%S"
#fmt = "%d/%m/%Y %H:%M"
#fmt = "%m/%d/%Y %H:%M:%S"

# Enter multiple dates in comma seperated

date_st = "1/21/2020 13:11:57,1/21/2020 13:30:44,1/21/2020 14:22:45,1/21/2020 14:26:13,1/21/2020 14:30:43"

date_spl = date_st.split(',')

for i in range(0, len(date_spl)):
    datetime_obj = datetime.strptime(date_spl[i], fmt)
    datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
    date_time_new = datetime_obj_utc + timedelta(hours=5)
    print(date_time_new.strftime("%Y-%m-%dT%H:%M:%S"))