n = int(input())
snowball_max = {}
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = pow((snowball_snow // snowball_time), snowball_quality)
    if not snowball_max:
        snowball_max['snowball_value'] = snowball_value
        snowball_max['snowball_snow'] = snowball_snow
        snowball_max['snowball_time'] = snowball_time
        snowball_max['snowball_quality'] = snowball_quality
    elif snowball_value > snowball_max['snowball_value']:
        snowball_max.clear()
        snowball_max['snowball_value'] = snowball_value
        snowball_max['snowball_snow'] = snowball_snow
        snowball_max['snowball_time'] = snowball_time
        snowball_max['snowball_quality'] = snowball_quality
print(
    f"{snowball_max['snowball_snow']} : {snowball_max['snowball_time']} = {snowball_max['snowball_value']} "
    f"({snowball_max['snowball_quality']})")
