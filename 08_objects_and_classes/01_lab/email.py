class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        if not self.is_sent:
            self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
list_with_emails = []

while command != "Stop":
    current_sender, current_receiver, current_content = command.split(" ")
    current_email_data = Email(current_sender, current_receiver, current_content)
    list_with_emails.append(current_email_data)
    command = input()

send_indices = [int(index) for index in input().split(", ")]
for i in send_indices:
    Email.send(list_with_emails[i])

for email in list_with_emails:
    print(Email.get_info(email))
