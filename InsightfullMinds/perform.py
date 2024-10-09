import praw
from textblob import TextBlob

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

# Function to analyze sentiment of comments
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Function to summarize sentiment
def analyze_post_sentiments(posts_data):
    sentiment_summary = {"positive": 0, "negative": 0, "neutral": 0}
    for post in posts_data:
        for comment in post['comments']:
            sentiment = analyze_sentiment(comment)
            sentiment_summary[sentiment] += 1
    return sentiment_summary

# Main code execution
if __name__ == "__main__":
    posts_data = get_subreddit_data('mentalhealth', 10)  # Fetch posts data
    sentiment_summary = analyze_post_sentiments(posts_data)  # Analyze sentiment

    # Print sentiment summary
    print(sentiment_summary)

