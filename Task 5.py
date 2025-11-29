import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
methods = ['GET', 'POST', 'PUT', 'DELETE']
all_methods = methods + ['HEAD', 'OPTIONS', 'PATCH', 'TRACE']

# 1. Запрос без параметра method
response_no_method = requests.get(url)
print("1. Без параметра method:")
print(f"Status: {response_no_method.status_code}")
print(f"Body: {response_no_method.text}\n")

# 2. Запрос с не из списка методов (например, HEAD)
response_unknown_method = requests.get(url, params={'method': 'HEAD'})
print("2. Неизвестный метод (HEAD):")
print(f"Status: {response_unknown_method.status_code}")
print(f"Body: {response_unknown_method.text}\n")

# 3. Запрос с правильным значением method
for method in methods:
    if method == 'GET':
        resp = requests.get(url, params={'method': method})
    elif method == 'POST':
        resp = requests.post(url, data={'method': method})
    elif method == 'PUT':
        resp = requests.put(url, data={'method': method})
    elif method == 'DELETE':
        resp = requests.delete(url, data={'method': method})
    else:
        continue
    print(f"3. Метод {method} с правильным параметром method:")
    print(f"Status: {resp.status_code}")
    print(f"Body: {resp.text}\n")

# 4. Цикл
for real_method in all_methods:
    # Перебираем все значения параметра method
    for param_method in methods:
        params = {'method': param_method}
        if real_method == 'GET':
            response = requests.get(url, params=params)
        elif real_method == 'POST':
            response = requests.post(url, data=params)
        elif real_method == 'PUT':
            response = requests.put(url, data=params)
        elif real_method == 'DELETE':
            response = requests.delete(url, data=params)
        elif real_method == 'HEAD':
            response = requests.head(url, params=params)
        elif real_method == 'OPTIONS':
            response = requests.options(url, params=params)
        elif real_method == 'PATCH':
            response = requests.patch(url, data=params)
        elif real_method == 'TRACE':
            response = requests.request('TRACE', url, params=params)
        else:
            continue

        # Анализируем ответ
        print(f"Реальный метод: {real_method}, Параметр method: {param_method}")
        print(f"Ответ: {response.text}")
        print(f"Статус: {response.status_code}")
