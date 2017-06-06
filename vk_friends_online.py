import os
from getpass import getpass

import vk


def get_online_friends(login, password, app_id):
    # Implementation notes:
    #   We will use friends.get instead of friends.getOnline.
    # The latter is inefficient and error-prone:
    # https://gist.github.com/patrnk/eba5ab7bf1704253cc01aa78bcb07005
    #   One friends.get request can only return 5000 friends,
    # whereas a user can have up to 10000 friends online. That's why we make a second request
    # (see https://vk.com/dev/friends.get).
    fields = ['first_name', 'last_name'] 
    friend_count_limit = 5000
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends = api.friends.get(fields=fields, count=friend_count_limit)
    if len(friends) == friend_count_limit:
        friends += api.friends.get(fields=fields, offset=friend_count_limit)
    return [friend for friend in friends if friend['online']]


def print_friend(friend):
    output_string_template = '* {first_name} {last_name}'
    output_string = output_string_template.format(
        first_name=friend['first_name'],
        last_name=friend['last_name'],
    )
    print(output_string)


if __name__ == '__main__':
    app_id = os.environ['VK_APP_ID']
    login = input('Login: ')
    password = getpass('Password: ')
    friends_online = get_online_friends(login, password, app_id)
    print("Here's your online friends:")
    for online_friend in friends_online:
        print_friend(online_friend)
