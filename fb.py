import getpass
import fbchat
from fbchat.models import *
import time

def main():
    client = fbchat.Client(input('Username: '), getpass.getpass())
    friends = client.searchForUsers(input('Who do you want to spam? '))
    friend_id = friends[0].uid
    script = open('no_line_script.txt')
    delay = float(input('Delay between each message: '))
    for i in range(count_lines()):
        line = script.readline().rstrip('\n').split(" ")
        for word in line:
            try:
                client.send(Message(text=word), thread_id=friend_id, thread_type=ThreadType.USER)
                print(f'Sending the word {word}')
                time.sleep(delay)
            except:
                print("Sorry, we've reached Facebook's spam limit.")
                break

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


