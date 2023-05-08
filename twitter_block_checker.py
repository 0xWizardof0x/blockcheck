import tweepy
import sys

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def check_block(user_a, user_b):
    try:
        # Check if User A's tweets are visible to User B
        api.user_timeline(screen_name=user_a, count=1)
        print(f"{user_b} can see {user_a}'s tweets. They are not blocked.")
    except tweepy.TweepError as e:
        if e.api_code == 136: # Error code for being blocked
            print(f"{user_b} is blocked by {user_a}.")
        elif e.api_code == 401: # Error code for private or suspended account
            print(f"{user_a}'s account is private or suspended. Unable to determine block status.")
        else:
            print("An unknown error occurred. Unable to check block status.")

if __name__ == "__main__":
    user_a = input("Enter the Twitter handle of User A (without @): ")
    user_b = input("Enter the Twitter handle of User B (without @): ")

    check_block(user_a, user_b)
