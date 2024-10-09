import matplotlib.pyplot as plt
from perform import analyze_post_sentiments, get_subreddit_data  # Import functions

# Fetching data from the subreddit and calculating sentiment
posts_data = get_subreddit_data('mentalhealth', 10)  # Fetch posts data
sentiment_summary = analyze_post_sentiments(posts_data)  # Analyze sentiment

# Function to plot sentiment distribution
def plot_sentiment_distribution(sentiment_summary):
    labels = sentiment_summary.keys()
    sizes = sentiment_summary.values()
    
    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.title("Sentiment Distribution")
    plt.show()

# Main code execution
if __name__ == "__main__":
    plot_sentiment_distribution(sentiment_summary)
