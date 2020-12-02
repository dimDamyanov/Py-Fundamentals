class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
line = input()
while line != 'Stop':
    data = line.split()
    email = Email(data[0], data[1], data[2])
    emails.append(email)
    line = input()
sent = list(map(int, input().split(', ')))
for x in sent:
    emails[x].send()
for e in emails:
    print(e.get_info())
