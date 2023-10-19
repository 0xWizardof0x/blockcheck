import tweepy

# Set up the tweepy authorization
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"

auth = tweepy.OAuthHandler(access_token, access_token_secret, bearer_token)

api = tweepy.API(auth)

# Function to get all followers of a user
def get_all_followers(screen_name):
    followers = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
        followers.extend(page)
    return followers

# Your screen name and the screen name of the user you've blocked
your_screen_name = "YOUR_SCREEN_NAME"
blocked_screen_name = "BLOCKED_USER_SCREEN_NAME"

your_followers = get_all_followers(your_screen_name)
blocked_user_followers = get_all_followers(blocked_screen_name)

# Check for overlaps
overlap_followers = set(your_followers).intersection(blocked_user_followers)

# Convert user IDs back to screen names
overlap_followers_screen_names = [api.get_user(user_id).screen_name for user_id in overlap_followers]

# Output the list
for screen_name in overlap_followers_screen_names:
    print("@" + screen_name)
