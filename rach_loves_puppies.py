#! /usr/bin/python3

# Rachmaninov learned how to store values in .txt files. He will put on "data.txt" every image he has already twtitted,
# in order not to twit it again. That's how cool he is.

import tweepy, time, random, os, json

consumer_key = "---I won't tell!---"
consumer_key_secret = "---I won't tell!---"
access_token = "---I won't tell!---"
access_token_secret = "---I won't tell!---"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

def create_data_file(path):
    if os.path.isfile(path) == False:
        os.mknod("data.txt")
        
def create_quote_data(path):
    if os.path.isfile(path) == False:
        os.mknod("quotedata.txt")

def store_updated_quotes(path, twitted_quote):
    with open(path, 'a') as outfile:
        json.dump(twitted_quote, outfile, ensure_ascii=False)

def store_updated_images(twitted_image):

    with open('data.txt', 'a') as outfile:
        json.dump(twitted_image, outfile, ensure_ascii=False)

def twit_random_image():

    data_path = "where/you/want/your/data.txt"
    image_path = "path_to_your_images_here"

    create_data_file(data_path)

    while True:
        try:
            random_image = random.choice(os.listdir(image_path))
            with open(data_path, "r") as infile:
                lecture = infile.read()
                if not random_image in lecture:
                        API.update_with_media(image_path + "/" + random_image) # This is done this way since 
                        # the API method needs not only the file name as a string, but its whole directory.
                        store_updated_images(random_image)
                        print('Updated.')
                        time.sleep(3600) #3600 is equivalent to an hour. You can make your program twit more or less.
                else:
                    print("Something happened A.")
                    continue
        except(tweepy.error.TweepError):
            print("Something happened B.")
            continue
            
def twit_random_quote():

    data_path = "path_to_a_data_file" # Path to the file where you'll store the quotes you've already twitted.
    text_path = "path_to_text" # Path to a .txt file where you should store your quotes. 
    # In order to work propperly, they should be store with no spaces, one quote per line, such as
    # xzx - Mark Twain
    # Something - Rachmaninov
    # Whatever - Grace Hopper,
    # etc. Can be done differently, but changes in the script would be needed.

    create_quote_data(data_path)

    while True:
        try: 
            with open(text_path, "r") as f:
                line_lecture = f.readlines()
            random_quote = random.choice(line_lecture)
            random_quote_stringcheck = '"' + random_quote + '"'
            with open(data_path, "r") as f:
                data_lecture = f.read()
                if not random_quote_stringcheck in data_lecture:
                    API.update_status(random_quote)
                    store_updated_quotes(data_path, random_quote)
                    print("Updated quote.")
                    break
                else:
                    continue
        except(tweepy.error.TweepError):
            print("Something happened D")
            continue

def run_twits():

    while True:
        twit_random_quote()
        twit_random_image()
        time.sleep(7200)

run_twits()
