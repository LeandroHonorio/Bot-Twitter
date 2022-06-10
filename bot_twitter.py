
import time
import autenticador
import logging

global last_id
last_id = 0

def logConfig():
    logging.basicConfig(
        level=logging.INFO, #INFO, WARNING
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("execution.log"),
            logging.StreamHandler()
            ]
    )

def mentions(api):
    logging.info('MENÇÃO CHAMADA')
    global last_id
    print(f'last_id {last_id}')
    if last_id != 0:
        response = api.mentions_timeline(since_id=last_id, include_entities=False)
    else:
        response = api.mentions_timeline(include_entities=False) 
       
    for tweet in response:
        dictTweet = {
            "IdTweet": tweet.id,
            "IdUser": tweet.user.id,
            "UserName": tweet.user.name,
            "ScreenName": tweet.user.screen_name,
            "Location": tweet.user.location,
            "TweetAt": tweet.created_at,
            "UploadTweet": tweet.source,
            "text": tweet.text
        }
        if tweet.in_reply_to_status_id_str == None:
        
            if not tweet.favorited:
                    # Mark it as Liked, since we have not done it yet
                    try:
                        tweet.favorite()
                        last_id = dictTweet['IdTweet']
                    except Exception as e: 
                        logging.error(f'ERROR NO FAV, {e}')            
            if not tweet.retweeted:
                    # Retweet, since we have not retweeted it yet
                    try:
                        tweet.retweet()
                        last_id = dictTweet['IdTweet']
                    except Exception as e: 
                        logging.error(f'ERROR NO Rt , {e}')    

def main():
    logConfig()
    api = autenticador.api_v1_oauth1() 

    while True:
        try:
            mentions(api)
            time.sleep(120)            
        except:
            logging.error('ERRO NA REQUISIÇÃO, AGURDANDO 600s')
            time.sleep(600)
                    
if __name__ == '__main__':
    main() 

    




