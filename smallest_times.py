import sys

times = ["17:21", "23:50", "17:19"]


def find_smallest_time_in_between(times):
	parsed_times = parse_times(times)

	parsed_times = sorted(parsed_times)
	
	min_diff = sys.maxint
	for i in range(len(parsed_times)):
		j = (i + 1) % len(parsed_times)

		diff = get_time_diff(parsed_times[i], parsed_times[j])

		min_diff = min(min_diff, diff)

	return min_diff


def parse_times(times):
	return map(lambda x: map(lambda y: int(y), x.split(':')), times)


def get_time_diff(i, j):
	hours_diff = abs(j[0] - i[0]) % 23

	if hours_diff == 0:
		mins_diff = i[1] - j[0]
	else: 
		mins_diff = (60 - i[1]) + j[1]

	return mins_diff + (hours_diff * 60)


print(find_smallest_time_in_between(times))