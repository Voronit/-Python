geo_logs = [
    {'visit1': ['Moscow', 'Russia']},
    {'visit2': ['Delhi', 'India']},
    {'visit3': ['Vladimir', 'Russia']},
    {'visit4': ['Lisbon', 'Portugal']},
    {'visit5': ['Paris', 'France']},
    {'visit6': ['Lisbon', 'Portugal']},
    {'visit7': ['Tula', 'Russia']},
    {'visit8': ['Tula', 'Russia']},
    {'visit9': ['Kursk', 'Russia']},
    {'visit10': ['Arkhangelsk', 'Russia']}
]

new_geo_logs = []

for log in geo_logs:
  if (list(log.values())[0][1]) == "Russia":
    new_geo_logs.append(log)

print(new_geo_logs)