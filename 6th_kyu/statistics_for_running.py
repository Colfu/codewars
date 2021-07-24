# You are the "computer expert" of a local Athletic Association (C.A.A.).
# Many teams of runners come to compete.
# Each time you get a string of all race results of every team who has run.
# For example here is a string showing the individual results of a team of 5 runners:
# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
#
# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds)
# are positive or null integer (represented as strings) with one or two digits. There are no traps in this format.
#
# To compare the results of the teams you are asked for giving three statistics; range, average and median.  ***Cr.1-3
# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3,
# and the highest is 9, so the range is 9 − 3 = 6.
# Mean or Average : To calculate mean, add together all of the numbers in a set and
# then divide the sum by the total count of numbers.
# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half.
# The median of a finite list of numbers can be found by arranging all the observations from lowest value
# to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5)
# when there is an odd number of observations.
# If there is an even number of observations, then there is no single middle value;
# the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).
#
# Your task is to return a string giving these 3 values. For the example given above, the string result will be
# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`
# where hh, mm, ss are integers (represented by strings) with each 2 digits.
#
# Remarks:
# if a result in seconds is ab.xy... it will be given truncated as ab.
# if the given string is "" you will return ""
# ---------------------------------

# Plan:
# convert each time to seconds
# perform calculaions
# convert back for answers

def stat(times_str):

    """
    To compare the results of the teams you are asked for giving three statistics; range, average and median.

    Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3,
    and the highest is 9, so the range is 9 − 3 = 6.

    Mean or Average : To calculate mean, add together all of the numbers in a set and
    then divide the sum by the total count of numbers.

    Median : In statistics, the median is the number separating the higher half of a data sample from the lower half.
    The median of a finite list of numbers can be found by arranging all the observations from lowest value
    to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5)
    when there is an odd number of observations.
    If there is an even number of observations, then there is no single middle value;
    the median is then defined to be the mean of the two middle values
    (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

    :param times_str: A string of times in the format hh|mm|ss
    :return: string in form of "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`
    where hh, mm, ss are integers (represented by strings) with each 2 digits
    """
    if len(times_str) == 0:
        return ""

    # split string into list so can access each time separately
    times_list = list(times_str.split(','))

    # convert each time into seconds
    times_in_seconds_list = []
    for time in times_list:
        part = time.split('|')
        hours = part[0]
        mins = part[1]
        secs = part[2]
        seconds = (int(hours)*3600 + int(mins)*60 + int(secs))
        times_in_seconds_list.append(seconds)

    # sort list into numerical order to be able to find results
    times_in_seconds_list.sort()

    def seconds_converter(seconds_input):
        """
        Convert an integer of seconds into the format hh|mm|ss

        :param seconds: interger
        :return: hh|mm|ss
        """

        seconds_input = int(seconds_input)
        sc_hours = seconds_input // 3600
        sc_mins = (seconds_input - (sc_hours * 3600)) // 60
        sc_secs = seconds_input - (sc_hours * 3600) - (sc_mins * 60)

        # Add leading 0's when number is single digit using str(string).zfill(width)
        converted_time = str(sc_hours).zfill(2) + '|' + str(sc_mins).zfill(2) + '|'+ str(sc_secs).zfill(2)

        return converted_time

    # Testing that the output of the seconds_converter function equals the input:
    # print('input is', times_str)
    # print('time in seconds is', times_in_seconds_list)
    # print('converted input is', seconds_converter(times_in_seconds_list[0]))

    # Find Range : The difference between the lowest and highest values, and convert back into hh|mm|ss   **Cr.1
    range_in_secs = times_in_seconds_list[-1] - times_in_seconds_list[0]
    range_in_hh_mm_ss = seconds_converter(range_in_secs)

    # Find Mean or Average : Add together all of the numbers in a set and divide by the total count of numbers.  **Cr.2
    average_in_secs = sum(times_in_seconds_list) / len(times_in_seconds_list)
    average_in_hh_mm_ss = seconds_converter(average_in_secs)

    # Find Median : The number separating the higher half of a data sample from the lower half.  **Cr.3
    if len(times_in_seconds_list) % 2 == 0:
        median_high = times_in_seconds_list[len(times_in_seconds_list)//2]
        median_low = times_in_seconds_list[len(times_in_seconds_list)//2 -1]
        median_in_secs = (median_high + median_low) // 2
    else:
        median_in_secs = times_in_seconds_list[len(times_in_seconds_list)//2]
    median_in_hh_mm_ss = seconds_converter(median_in_secs)

    return 'Range: ' + range_in_hh_mm_ss + ' Average: ' + average_in_hh_mm_ss + ' Median: ' + median_in_hh_mm_ss


# some tests:
# print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"),
#       "Should be = Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")
# print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"),
#       "Should be = Range: 00|31|17 Average: 02|26|18 Median: 02|22|00")
