#!/usr/bin/env python3
"""Task 02 – Interact with JSONPlaceholder using requests."""
import csv, requests
URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts() -> None:
    resp = requests.get(URL, timeout=10)
    print(f"Status Code: {resp.status_code}")
    if resp.ok:
        for post in resp.json():
            print(post["title"])

def fetch_and_save_posts(csv_file: str = "posts.csv") -> None:
    resp = requests.get(URL, timeout=10)
    if not resp.ok:
        print(f"Request failed ({resp.status_code})")
        return
    posts = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in resp.json()]
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        w.writeheader(); w.writerows(posts)
    print(f"Saved {len(posts)} posts → {csv_file}")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
