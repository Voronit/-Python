l = ['2018-01-01', 'yandex', 'cpc', 100]

def fun(dictionary):
  if len(dictionary) == 1:
    return dictionary[0]
  else:
    return {dictionary[0]:  fun(dictionary[1:])}
    
print (fun(l))