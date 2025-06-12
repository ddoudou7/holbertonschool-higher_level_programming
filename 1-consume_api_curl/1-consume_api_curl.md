# 1. Consume data from an API with `curl`

## Vérifier curl

```bash
curl --version
```

## Exemples JSONPlaceholder

```bash
# GET all posts
curl https://jsonplaceholder.typicode.com/posts | jq .

# GET one post
curl https://jsonplaceholder.typicode.com/posts/42 | jq .

# HEADERS only
curl -I https://jsonplaceholder.typicode.com/posts

# POST (fake create)
curl -X POST https://jsonplaceholder.typicode.com/posts      -H "Content-Type: application/x-www-form-urlencoded"      -d "title=foo&body=bar&userId=1" | jq .
```

