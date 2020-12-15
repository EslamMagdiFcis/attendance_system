import json

from connect_database import execute_query
from uitls import datetime_utc_format, format_date, format_datetime


def get_attendance_history(empylee_code):

    sql_query = """
                SELECT 
                    a.day, 
                    actions.Action, 
                    actions.ActionTime
                FROM 
                    Attendance a
                    INNER JOIN AttendanceActions actions ON  a.Id = actions.AttendanceId
                WHERE
                    lower(a.employee) = '{empylee_code}'
                ORDER BY
	                actions.Id  
            """.format(empylee_code=empylee_code.lower())
    
    result = execute_query(sql_query)

    days = []
    days_set = sorted(set([day for day, _, _ in result]))

    for day_set in days_set:
        actions = []

        for _, action, action_time in result:
            action_time = format_datetime(action_time)
            action_time = datetime_utc_format(action_time)

            if format_date(day_set) == action_time.date():
                actions.append({"action": action, "time": action_time.isoformat() })


        days.append({"date": day_set, "actions": actions})

    return json.dumps({"days": days})
