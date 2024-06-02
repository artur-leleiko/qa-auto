import requests


class GitHub:
    def get_user(self, username: str):
        url = f"https://api.github.com/users/{username}"
        request = requests.get(url)
        body = request.json()

        return body

    def search_repo(self, name: str):
        request = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": {name}}
        )
        body = request.json()

        return body

    def search_organization(self, name: str):
        url = f"https://api.github.com/orgs/{name}"
        request = requests.get(url)
        body = request.json()

        return body

    def search_topic(self, name: str, per_page: int = 30):
        request = requests.get(
            "https://api.github.com/search/topics",
            params={"q": {name}, "per_page": {per_page}}
        )
        body = request.json()

        return body
