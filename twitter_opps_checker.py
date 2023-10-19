import tweepy

# Your credentials
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Set up Tweepy with OAuth1a
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_user_id(screen_name):
    """Retrieve the user ID for a screen name using Tweepy."""
    user = api.get_user(screen_name=screen_name)
    return user.id_str

def get_followers(user_id):
    """Retrieve followers for a user ID using Tweepy."""
    followers = []
    for follower in tweepy.Cursor(api.get_follower_ids, user_id=user_id).items():
        followers.append(follower)
    return followers

if __name__ == "__main__":
    YOUR_SCREEN_NAME = "you"
    BLOCKED_SCREEN_NAME = "opps"
    
    # Convert screen names to user IDs
    YOUR_USER_ID = get_user_id(YOUR_SCREEN_NAME)
    BLOCKED_USER_ID = get_user_id(BLOCKED_SCREEN_NAME)
    
    your_followers = get_followers(YOUR_USER_ID)
    blocked_followers = get_followers(BLOCKED_USER_ID)
    
    overlapping_followers = set(your_followers).intersection(set(blocked_followers))
    print("Overlapping follower IDs:", overlapping_followers)
