import praw

# Reddit API credentials
reddit = praw.Reddit(
    client_id='6e3Op2hNfb4bdfT2B5CovQ',
    client_secret='rs6rYv7NJSL7mxt8X-fZ7Vs-vNXaLA',
    user_agent='sentimentanalyser/1.0 by alina'
)

# Function to scrape data from a subreddit
def get_subreddit_data(subreddit_name, num_posts):
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []
    
    # Get the top num_posts from the subreddit
    for submission in subreddit.top(limit=num_posts):
        post = {
            "title": submission.title,
            "body": submission.selftext,
            "comments": []
        }
        
        submission.comments.replace_more(limit=0)  # Avoid limit errors
        for comment in submission.comments.list():
            post['comments'].append(comment.body)
        
        posts_data.append(post)
    return posts_data

# Main code execution
if __name__ == "__main__":
    posts_data = get_subreddit_data('mentalhealth', 10)  # Fetch posts data

    # Print the titles of fetched posts
    for post in posts_data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")

