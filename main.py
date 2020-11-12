from get_token import getToken
import argparse

password = None

def main(args):    
    # Get telegram token and get the corresponding bot
    token = getToken(args.salt_path, args.token_path, password=password)
    print('Token successfully acquired')

if __name__ == '__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument('--salt_path', type=str, default='salt.pickle')
    parser.add_argument('--token_path', type=str, default='token.pickle')
    parser.add_argument('--verbose', '-v', action='store_true')  

    args = parser.parse_args()

    main(args)