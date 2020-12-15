from datetime import datetime

from db_context import execute_query
from uitls import format_date, format_datetime, round_time


def get_attendance(empylee_code, date):

    try:
        date = format_date(date)
    except:
        print('Please, enter valid date your input "{}"'.format(date))
        print('hint: "2020-04-09" is only vaild date format')
        return {}

    ATTENDED_TEXT = 'attended'
    DURATION_TEXT = 'duration'

    sql_query = """
                    SELECT 
                        actions.ActionTime,
                        actions.Action
                    FROM 
                        Attendance a
                        INNER JOIN AttendanceActions actions ON  a.Id = actions.AttendanceId
                    WHERE
                        lower(a.employee) = '{empylee_code}'
                        AND a.day = '{date}'
                    ORDER BY
                        actions.Id
                """.format(empylee_code=empylee_code.lower(), date=date)

    result_set = execute_query(sql_query)

    result_set_len = len(result_set)
 
    if result_set_len == 0:   
        return {ATTENDED_TEXT: False, DURATION_TEXT: '00:00'}

    total_hour_per_day = datetime.min

    CHECK_IN_STATE = 'checkin'

    last_row_index = result_set_len - 1
    checkin_date = None

    for index, row in enumerate(result_set):
        action_time, action = row

        action_time = format_datetime(action_time)

        if action.lower() == CHECK_IN_STATE:
            checkin_date = action_time
            is_last_action_check_in = index == last_row_index

            if is_last_action_check_in:
                day_midnight_time = datetime.combine(action_time, datetime.max.time())
                total_hour_per_day +=  day_midnight_time - action_time

        else:
            is_check_in_before_check_out = checkin_date is not None

            if is_check_in_before_check_out:
                total_hour_per_day += action_time - checkin_date
            else:
                day_start_time = datetime.combine(action_time, datetime.min.time())
                total_hour_per_day += action_time - day_start_time

    result = round_time(total_hour_per_day.time())

    if result.hour == 0 and result.minute == 0:
        return {ATTENDED_TEXT: False, DURATION_TEXT: '00:00'}

    duration =  '{h:02d}:{m:02d}'.format(h=result.hour, m=result.minute)
    return { ATTENDED_TEXT: True, DURATION_TEXT: duration }
