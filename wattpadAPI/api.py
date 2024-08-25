
import requests
from .exceptions import WattpadAPIError, RateLimitError
from .models import Story, Chapter, Comment
from .utils.decorators import rate_limit
from .config import API_BASE_URL, API_BASE_URL_v2, API_BASE_URL_v3, API_BASE_URL_v5

class WattpadAPI:
    def __init__(self, api_key=None):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'WattpadAPI/1.0',
            'Authorization': f'{api_key}' if api_key else None
        })

    @rate_limit(max_calls=5, time_frame=1)
    def _make_request(self, endpoint, method='GET', params=None, data=None, requires_auth=True, api_base_url=API_BASE_URL):
        url = f"{api_base_url}/{endpoint}"
        if requires_auth and not self.session.headers.get('Authorization'):
            raise WattpadAPIError("This endpoint requires authentication. Please provide an API key.")

        response = self.session.request(method, url, params=params, json=data)

        if response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        elif response.status_code != 200:
            raise WattpadAPIError(f"API request failed: {response.status_code}")

        return response.json()

    def story(self, story_id):
        data = self._make_request(f'stories/{story_id}', requires_auth=False, api_base_url=API_BASE_URL_v3)
        return Story(data)

    def get_chapter(self, chapter_id):
        data = self._make_request(f'parts/{chapter_id}', requires_auth=False)
        return Chapter(data)

    def search_stories(self, query, limit=20, offset=0):
        params = {'query': query, 'limit': limit, 'offset': offset}
        data = self._make_request('stories', params=params, requires_auth=False)
        return [Story(story_data) for story_data in data.get('stories', [])]

    def get_story_comments(self, story_id, limit=20, offset=0):
        params = {'limit': limit, 'offset': offset}
        data = self._make_request(f'/comments/namespaces/parts/resources/{story_id}/comments', params=params, requires_auth=False, api_base_url=API_BASE_URL_v5)
        return [Comment(comment_data) for comment_data in data.get('comments', [])]
