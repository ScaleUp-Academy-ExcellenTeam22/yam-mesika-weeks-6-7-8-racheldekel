class PostOffice:
    """A Post Office class. Allows users to message each other.
    Args:
        usernames (list): Users for which we should create PO Boxes.
    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.
                Args:
                    sender (str): The message sender's username.
                    recipient (str): The message recipient's username.
                    message_body (str): The body of the message.
                    urgent (bool, optional): The urgency of the message.
                                            Urgent messages appear first.
                Returns:
                    int: The message ID, auto incremented number.
                Raises:
                    KeyError: If the recipient does not exist.
                Examples:
                    After creating a PO box and sending a letter,
                    the recipient should have 1 message in the
                    inbox.
                    >>> po_box = PostOffice(['a', 'b'])
                    >>> message_id = po_box.send_message('a', 'b', 'Hello!')
                    >>> len(po_box.boxes['b'])
                    1
                    >>> message_id
                    1
                """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N=10):
        """
        A function that gets the name of the user and number of the message request.
        The function returns the first N messages in the mailbox.
        :param username: name of the user
        :param N: number of the message request
        :return: the first N messages in the mailbox. (if not exist return all messages in the mailbox)
        """
        return_message = []
        count_message = 0
        if not N == 0:
            if N < len(self.boxes[username]):
                for message in range(len(self.boxes[username])):
                    if self.boxes[username][message].message_details['status'] == 'not read':
                        self.boxes[username][message].message_details['status'] == 'read'
                        count_message = count_message + 1
                        return_message.append(self.boxes[username][message])
                    if count_message == N:
                        break

        for message in range(len(self.boxes[username])):
            if self.boxes[username][message].message_details['status'] == 'not read':
                self.boxes[username][message].message_details['status'] == 'read'
                return_message.append(self.boxes[username][message])
        return return_message

    def search_inbox(self, username, sentence):
        """
        A function that gets the name of the user and string .
        The function return list of all the messages that contains the string in there headline or font.
        :param username:  the name of the user
        :param sentence:  string
        :return: list of all the messages that contains the string in there headline or font.
        """
        return_message = []
        for message in self.boxes[username]:
            if sentence in message.message_details['body'] or sentence in message.message_details['sender']:
                return_message.append(message)

        return return_message


class Message:
    """
    class message - print and help with the details.
    """


def __init__(self, message_id, message_body, message_sender, message_status="not read"):
    """
    The init function that dave the information of the message that necessary.
    :param self:
    :param message_id:
    :param message_body:
    :param message_sender:
    :param message_status:
    :return:
    """
    self.id = message_id
    self.body = message_body
    self.sender = message_sender
    self.status = message_status


def __str__(self):
    """
    Function that prints the message.
    """
    return self.sender, self.body


def len(self):
    """
    Funstion that returns the length of the message.
    """
