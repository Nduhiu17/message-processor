import math


class ProcessMessage:

    def __init__(self, msg):
        self.msg = msg
        self.word_count = 0

        self.message()

    def message(self):
        words = self.msg.split(" ")
        data = {}

        for index, item in enumerate(words):
            self.word_count += len(item)
            data[index] = self.word_count

            a = self.process_msg(0, 155, data, words, 1)
            b = self.process_msg(155, 315, data, words, 2)
            c = self.process_msg(315, 475, data, words, 3)
            d = self.process_msg(475, 635, data, words, 4)
            e = self.process_msg(635, 795, data, words, 5)
            f = self.process_msg(795, 955, data, words, 6)
            g = self.process_msg(955, 1155, data, words, 7)
            h = self.process_msg(1155, 1275, data, words, 8)
            i = self.process_msg(1275, 1435, data, words, 9)
        subdivided_messages = [a, b, c, d, e, f, g, h, i]
        for sms in subdivided_messages:
            if len(sms) > 6:
                print(sms)

    def process_msg(self, cond_min, cond_max, data, words, position):
        lists = []
        for key, val in data.items():
            if cond_min < val < cond_max:
                lists.append(words[key])

        str1 = ' '.join(lists)

        total = math.ceil(self.word_count / 154)
        suffix = ' ({}/{})'.format(position, total)
        message = str1 + suffix
        return message


MSG = """
A company has hired you as a consultant to develop software that can be used for
sending SMS to their end-users. Currently, the maximum number of characters possible
for one message is 160. Some of the messages the company sends contain more than
160 characters and need to be broken up into smaller chunks.

The company has expressed concerns that when sending messages in different chunks
there is no guarantee that the messages will be delivered to the end-user’s phone in
order. To circumvent this problem, the company would like to add pagination to the end
of the message to give proper context to the end-user if needed.
A company has hired you as a consultant to develop software that can be used for
sending SMS to their end-users. Currently, the maximum number of characters possible
for one message is 160. Some of the messages the company sends contain more than
160 characters and need to be broken up into smaller chunks.

The company has expressed concerns that when sending messages in different chunks
there is no guarantee that the messages will be delivered to the end-user’s phone in
order. To circumvent this problem, the company would like to add pagination to the end
of the message to give proper context to the end-user if needed.
"""

ProcessMessage(MSG)
