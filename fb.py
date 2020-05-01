import getpass
import fbchat
from fbchat.models import *
import time

def main():
    client = fbchat.Client(input('Username: '), getpass.getpass())
    user_choice = input('Do you want to spam a user or a groupchat? ').lower()

    while user_choice not in ['user', 'groupchat']:
        user_choice = input('Please enter valid answer (user/groupchat)').lower()

    if user_choice == 'user':
        friends = client.searchForUsers(input('Who do you want to spam? '))
        thread_id = friends[0].uid
        thread_type = ThreadType.USER
    else:
        groups = client.searchForGroups(input('Which group do you want to spam? '))
        thread_id = groups[0].uid
        thread_type = ThreadType.GROUP
    delay = float(input('Delay between each message: '))
    script = open('no_line_script.txt')
    for i in range(count_lines()):
        line = script.readline().rstrip('\n').split(" ")
        for word in line:
            try:
                client.send(Message(text=word), thread_id=thread_id, thread_type=thread_type)
                print(f'Sending the word {word}')
                time.sleep(delay)
            except:
                print("Sorry, we've reached Facebook's spam limit.")
    script.close()
    client.logout()

def count_lines(file='no_line_script.txt'):
    with open(file, 'r') as file:
        for index, line in enumerate(file):
            pass
    file.close()
    return index + 1

def remove_lines(original='script.txt', empty='no_line_script.txt'):
    script = open(original, 'r')
    empty_script = open(empty, 'w')

    script_length = count_lines(original)
    for i in range(script_length):
        line = script.readline()
        if line.replace(" ","") not in ['\n','\r\n']:
            empty_script.write(line)

if __name__ == '__main__':
    remove_lines()
    main()


