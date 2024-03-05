"""
Ein Satz soll geschrieben werden.
Jedes Wort wird in ein dict gesetzt mit dem value
aus wie vielen char das Wort vesteht

"""
sentence = input()

result = {key: len(key) for key in sentence.split()}

print(result)


"""
Berechnen von C in F
(temp_c * 9/5) + 32 = temp_f
"""
weather_dict = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}


def convert_f(temp_c):
    return (temp_c * 9/5) + 32


weather_f = {day: convert_f(temp) for (day, temp) in weather_dict.items()}

print(weather_f)
