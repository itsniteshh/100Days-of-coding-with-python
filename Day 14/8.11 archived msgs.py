msgs = ["Hello", "good morning", "bonjour", "You look beautiful"]
sent_msgs = []

def sending_messages(msgs, sent_msgs, name=""):
    while msgs:
        sending = msgs.pop()
        print(f"The msg '{sending}' is being sent to {name}")
        sent_msgs.append(sending)


def sent_messages(semt_msgs):
    for msg in sent_msgs:
        print(msg)

sending_messages(msgs, sent_msgs, "Purnima")
print(f"\nThe following messages are sent: ")
sent_messages(sent_msgs)

print(sending_messages(sent_msgs[:], msgs))