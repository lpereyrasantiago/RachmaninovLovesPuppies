#! /usr/bin/python3

# Rachmaninov learned how to store values in .txt files. He will put on "data.txt" every image he has already twtitted,
# in order not to twit it again. That's how cool he is.

# Rachmaninov learned how to send a private message to somebody he likes. He can now choose a random line from a given
# .txt file and send it privately trough twitter. This has a 10% chances to happen: thus we avoid spam!!

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

def store_updated_love(path, texted):
    with open(path, 'a') as outfile:
        json.dump(texted, outfile, ensure_ascii=False)

def create_phrase_data(path):
    if os.path.isfile(path) == False:
        os.mknod("phrasedata.txt")

def twit_random_quote():
    
     # The function chooses a single line from a .txt file to updated as status, so it should probably contain
    # one quote per line. This function can be tweaked in order not to update only a line, that's up
    # to anybody, though you should be careful not to exceed twitter's max characters limit.

    data_path = "path to a .txt where to store the updated quotes."
    text_path = "path to .txt file containing the quotes, one per line."

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


def twit_random_image():

    data_path = "path to .txt file where to store updated images"
    image_path = "path to images folder"

    create_data_file(data_path)

    while True:
        try:
            random_image = random.choice(os.listdir(image_path))
            with open(data_path, "r") as infile:
                lecture = infile.read()
                if not random_image in lecture:
                    API.update_with_media(image_path + "/" + random_image) # This is done this way since the API method needs not only the file name as a string, but its directory too.
                    store_updated_images(random_image)
                    print('Updated.')
                    break
                else:
                    print("Something happened A.")
                    continue
        except(tweepy.error.TweepError):
            print("Something happened B.")
            continue

def send_phrase_message():
    
    # The function chooses a single line from a .txt file to send as a message, so it should probably contain
    # phrases (one phrase per line). This function can be tweaked in order not to send only a line, that's up
    # to anybody.

    path = "path to the .txt file where the phrases are, one per line."
    phrase_data_path = "path to a data .txt file where the sent phrases will be recorded"
   
    addressee_id = some_id_as_string
    addresse_user = some_user_name_as_string
    addressee_screenname = some_screenname_as_string

    create_phrase_data(phrase_data_path)
    intro = "Some intro, such as: Hello, pretty girl! Here's something my creator wanted to tell you... \n\n"

    thrown_chance = random.randint(0, 9) # Throws a random number between 0 and 9.
    print(str(thrown_chance))

    if thrown_chance == 4: # If the number is 4, sends the message. This makes a 10% probability of a message being sent.
        # Avoiding spam is a good deed!
        while True:
            try:
                with open(path, 'r') as infile:
                    lecture = infile.readlines()
                random_phrase = random.choice(lecture)
                random_phrase_stringcheck = '"' + random_phrase + '"'
                with open(phrase_data_path, 'r') as f:
                    data_lecture = f.read()
                    if not random_phrase_stringcheck in data_lecture:
                        love_message = intro + random_phrase
                        API.send_direct_message(addressee_user, addressee_screenname, addressee_id, love_message)
                        store_updated_love(phrase_data_path, random_phrase)
                        break
                    else:
                        continue
            except IndexError:
                continue
    


def run_twits():

    while True:
        twit_random_quote()
        twit_random_image()
        send_phrase_message()
        time.sleep(7200)

run_twits()
