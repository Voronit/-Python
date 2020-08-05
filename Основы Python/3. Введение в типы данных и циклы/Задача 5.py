stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

i = 0

for q in stats:
  if stats[q] > i:
    i = stats[q]
    key = q

print("'" + key + "'")