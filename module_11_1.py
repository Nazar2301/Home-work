import requests

# Метод status_code объекта Response возвращает код состояния HTTP-ответа.
# Например, 200 означает успешный запрос, 404 - не найдено, и т.д.
response = requests.get('https://api.github.com')
print(response.status_code)

# Позволяет получить список репозиториев пользователя GitHub.
username = 'Nazar2301'
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(f"Repo: {repo['name']} - URL: {repo['html_url']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Позволяет получить и вывести содержимое веб-страницы.
response = requests.get('https://www.github.com')
print(response.text)
