def add_time(start_time, duration_time, starting_day=''):
    period_cycle = {'AM': 'PM', 'PM': 'AM'}
    days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, '': 0}
    start_hour_min, period = start_time.split(' ')
    start_hour, start_min = start_hour_min.split(':')
    duration_hour, duration_min = duration_time.split(':')
    sum_time = lambda x, y: int(x) + int(y)
    final_hour = sum_time(duration_hour, start_hour)
    final_min = sum_time(duration_min, start_min)
    days_passed = 0
    current_day = days[starting_day.lower()]

    if int(start_min) >= 60 or int(duration_min) >= 60:
        return 'Error: minutes have to be a number lower than 60'
    elif int(start_hour) > 12:
        return 'Error: starting time not have an hour larger than 12'
    elif period not in ['AM', 'PM']:
        return 'Error: {} is not a valid period of the day'.format(period)

    if final_min >= 60:#
        if final_hour + 1 == 12:
            if period_cycle[period] == 'AM':
                days_passed += 1
            period = period_cycle[period]
        if final_hour + 1 > 12:
            if period_cycle[period] == 'AM':
                days_passed += 1
            period = period_cycle[period]
            final_hour -= 12
        final_min -= 60
        final_hour += 1
        print(final_hour, period)

    while final_hour > 12:
        if final_hour == 24:
            final_hour = 12
            days_passed += 1
        elif period_cycle[period] == 'AM':
            period = period_cycle[period]
            days_passed += 1
            final_hour -= 12
        else:
            period = period_cycle[period]
            final_hour -= 12

    final_min = '0{}'.format(final_min) if final_min < 10 else str(final_min)
    final_time = str(final_hour) + ':' + final_min + ' {}'.format(period)

    if current_day != 0 and days_passed != 0:
        current_day += days_passed
        while current_day > 7:
            current_day -= 7
        final_time += ', {}'.format(list(days.keys())[list(days.values()).index(current_day)].capitalize())
    elif current_day != 0:
        final_time += ', {}'.format(list(days.keys())[list(days.values()).index(current_day)].capitalize())

    if days_passed == 1:
        final_time += ' (next day)'
    elif days_passed > 1:
        final_time += ' ({} days later)'.format(days_passed)

    return final_time

