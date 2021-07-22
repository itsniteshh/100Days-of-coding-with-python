original_messages = ["Hello", "good morning", "bonjour", "You look beautiful"]
sent_messages = []

def send_messages(original_messages, sent_messages, name):
    while original_messages:
        sending_msg = original_messages.pop()
        print(f"The msg '{sending_msg}' is being sent to {name}")
        sent_messages.append(sending_msg)


def final_messages(semt_messages):
    for msg in sent_messages:
        print(msg)

send_messages(original_messages, sent_messages, "Purnima")
print(f"\nThe following messages are sent: ")
final_messages(sent_messages)
