def period_iterator(year:list,start_m:int, stop_m:int)->list:
    """
    year list of strings
    """
    YEAR = year
    MONTH =  [str(i) if i>9 else "0" + str(i) for i in range(start_m, stop_m +1)]

    periods = []

    for i in YEAR:
        for j in MONTH:
            k = i+j
            periods.append(k)
    # print(periods)
    return periods
