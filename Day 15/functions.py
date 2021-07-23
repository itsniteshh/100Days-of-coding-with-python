
messages = ["hie", "good morning", "hellow", "bonjour"]
sent_msgs = []


def send_msgs(messages, sent_msgs):

    while messages:
        sending_msg = messages.pop()
        print(f"The message  {sending_msg} is being sent right now.")
        sent_msgs.append(sending_msg)

def show_msgs(sent_msgs):

    print("\nThe following messages have been received: ")
    for msg in sent_msgs:
        print(msg)


send_msgs(messages, sent_msgs)
show_msgs(sent_msgs)



