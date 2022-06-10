# May 18.2022

def show_messages(messages):
    """Prints a list of messages."""
    for message in messages:
        print(message)

def send_messages(messages):
    """Prints a list of messages and copies them to a new list."""
    sent_messages = []
    while messages:
        sent_message = messages.pop()
        sent_messages.append(sent_message)
    print(sent_messages)
    for message in sent_messages:
        print(message)

text_messages = ['hello', 'a/s/l', 'hi bby', 'fuk you']

print(text_messages)
print('----------')
send_messages(text_messages[:])
print('++++++++++')
print(text_messages)
