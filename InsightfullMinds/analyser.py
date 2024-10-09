import praw

# Reddit API credentials
reddit = praw.Reddit(
    client_id='6e3Op2hNfb4bdfT2B5CovQ',
    client_secret='rs6rYv7NJSL7mxt8X-fZ7Vs-vNXaLA',
    user_agent='sentimentanalyser/1.0 by alina'
)

# Access the subreddit
subreddit = reddit.subreddit('mentalhealth')

# Fetch top 5 posts
for submission in subreddit.top(limit=5):
    print(f"Title: {submission.title}\n")
    print(f"Body: {submission.selftext}\n")
    print("-" * 40)
