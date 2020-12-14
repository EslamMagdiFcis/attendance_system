from get_attendance import get_attendance
from get_attendance_history import get_attendance_history


if __name__ == "__main__":
    print('----------------------------------------')
    print(get_attendance('emp01', '2020-04-01'))
    print(get_attendance('emp01', '2020-04-02'))
    print(get_attendance('emp01', '2020-04-03'))
    print(get_attendance('emp01', '2020-04-04'))
    print(get_attendance('emp01', '2020-04-05'))
    print(get_attendance('emp01', '2020-04-059'))
    print(get_attendance('emp02', '2020-04-03'))
    print(get_attendance('emp01', '2020-04-22'))
    print('----------------------------------------')

    print(get_attendance_history('emp01'))
    print('----------------------------------------')
    print(get_attendance_history('emp02'))
    print('----------------------------------------')