<div style="background-color: #ffcccc; border-left: 6px solid #ff0000; padding: 10px;">
<strong>⚠️ Warning:</strong> Because I did not care to make documention the docs has been written by AI and may have some issues with it. You have been warned and please fix any that you find.
</div>

<br>

<div style="background-color: #ffcccc; border-left: 6px solid #ff0000; padding: 10px;">
<strong>⚠️ Warning:</strong> I have not really made python packages or ever did anything like this before so don't clown on me if I did anything wrong and please just fix it or leave it alone and don't be rude about it.
</div>

# Wattpad API Wrapper Documentation

## Table of Contents

1. [Introduction](#introduction)
3. [Getting Started](#getting-started)
4. [API Reference](#api-reference)
   - [WattpadAPI](#wattpadapi)
   - [Story](#story)
   - [Chapter](#chapter)
   - [Comment](#comment)
   - [User](#user)
5. [Exception Handling](#exception-handling)
6. [Rate Limiting](#rate-limiting)
7. [Examples](#examples)

## Introduction

This Wattpad API wrapper provides a convenient way to interact with the Wattpad API, allowing you to retrieve information about stories, chapters, comments, and users on the Wattpad platform.

## Getting Started

To use the Wattpad API wrapper, you'll need to import the `WattpadAPI` class and create an instance:

```python
from wattpad_api import WattpadAPI

# Initialize the API client
api = WattpadAPI(api_key='your_api_key_here')
```

Note: Some endpoints don't require authentication, so you can omit the `api_key` if you're only using those endpoints.

## API Reference

### WattpadAPI

The main class for interacting with the Wattpad API.

#### Methods

##### `story(story_id)`

Retrieve information about a specific story.

- Parameters:
  - `story_id` (int): The ID of the story to retrieve.
- Returns: A `Story` object.

Example:
```python
story = api.story(1234567)
print(story.title)
```

##### `get_chapter(chapter_id)`

Retrieve information about a specific chapter.

- Parameters:
  - `chapter_id` (int): The ID of the chapter to retrieve.
- Returns: A `Chapter` object.

Example:
```python
chapter = api.get_chapter(9876543)
print(chapter.title)
```

##### `search_stories(query, limit=20, offset=0)`

Search for stories based on a query.

- Parameters:
  - `query` (str): The search query.
  - `limit` (int, optional): The maximum number of results to return. Default is 20.
  - `offset` (int, optional): The offset for pagination. Default is 0.
- Returns: A list of `Story` objects.

Example:
```python
results = api.search_stories("fantasy", limit=10)
for story in results:
    print(story.title)
```

##### `get_story_comments(story_id, limit=20, offset=0)`

Retrieve comments for a specific story.

- Parameters:
  - `story_id` (int): The ID of the story to retrieve comments for.
  - `limit` (int, optional): The maximum number of comments to return. Default is 20.
  - `offset` (int, optional): The offset for pagination. Default is 0.
- Returns: A list of `Comment` objects.

Example:
```python
comments = api.get_story_comments(1234567, limit=5)
for comment in comments:
    print(comment.text)
```

### Story

Represents a Wattpad story.

#### Attributes

- `id` (int): The story's unique identifier.
- `title` (str): The title of the story.
- `description` (str): The story's description.
- `cover_url` (str): URL of the story's cover image.
- `url` (str): The story's URL on Wattpad.
- `read_count` (int): Number of reads for the story.
- `vote_count` (int): Number of votes for the story.
- `comment_count` (int): Number of comments on the story.
- `parts` (list): A list of `Chapter` objects representing the story's chapters.

### Chapter

Represents a chapter in a Wattpad story.

#### Attributes

- `id` (int): The chapter's unique identifier.
- `title` (str): The title of the chapter.
- `url` (str): The chapter's URL on Wattpad.
- `create_date` (str): The date the chapter was created.
- `modify_date` (str): The date the chapter was last modified.
- `read_count` (int): Number of reads for the chapter.
- `vote_count` (int): Number of votes for the chapter.
- `comment_count` (int): Number of comments on the chapter.

### Comment

Represents a comment on a Wattpad story or chapter.

#### Attributes

- `resource` (Resource): Information about the resource the comment is on.
- `user` (User): The user who made the comment.
- `comment_id` (CommentId): The comment's unique identifier.
- `text` (str): The content of the comment.
- `created` (datetime): The date and time the comment was created.
- `modified` (datetime): The date and time the comment was last modified.
- `status` (str): The status of the comment.
- `sentiments` (dict): Sentiment information for the comment.
- `reply_count` (int): Number of replies to the comment.
- `labels` (list): Labels associated with the comment.
- `deeplink` (str): A deep link to the comment.

### User

Represents a Wattpad user.

#### Attributes

- `name` (str): The user's name.
- `avatar` (str): URL of the user's avatar image.

## Exception Handling

The wrapper defines two custom exceptions:

- `WattpadAPIError`: Raised for general API errors.
- `RateLimitError`: Raised when the API rate limit is exceeded.

Example of handling exceptions:

```python
from wattpad_api.exceptions import WattpadAPIError, RateLimitError

try:
    story = api.story(1234567)
except RateLimitError:
    print("Rate limit exceeded. Please wait before making more requests.")
except WattpadAPIError as e:
    print(f"An API error occurred: {str(e)}")
```

## Rate Limiting

The wrapper implements rate limiting to prevent exceeding the API's rate limits. By default, it allows 5 calls per second. If you exceed this limit, a `RateLimitError` will be raised.

## Examples

### Retrieving a Story and Its Chapters

```python
api = WattpadAPI()

# Get a story
story = api.story(1234567)
print(f"Title: {story.title}")
print(f"Description: {story.description}")
print(f"Read Count: {story.read_count}")

# Print information about each chapter
for chapter in story.parts:
    print(f"Chapter: {chapter.title}")
    print(f"Read Count: {chapter.read_count}")
    print(f"URL: {chapter.url}")
    print("---")
```

### Searching for Stories

```python
api = WattpadAPI()

# Search for fantasy stories
results = api.search_stories("fantasy", limit=5)

for story in results:
    print(f"Title: {story.title}")
    print(f"URL: {story.url}")
    print(f"Votes: {story.vote_count}")
    print("---")
```

### Retrieving Comments

```python
api = WattpadAPI()

# Get comments for a story
comments = api.get_story_comments(1234567, limit=10)

for comment in comments:
    print(f"User: {comment.user.name}")
    print(f"Comment: {comment.text}")
    print(f"Created: {comment.created}")
    print("---")
```

This documentation provides a comprehensive overview of the Wattpad API wrapper, including its classes, methods, and usage examples. Users can refer to this documentation to understand how to interact with the Wattpad API using this wrapper.