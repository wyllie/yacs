#!/usr/bin/env python3

# Yacs 1.0 (Yet Another CowSay)
# A very simple version of Cowsay written in Python
# Andrew Wyllie (c) 2018

# Original perl version: (c) 1999-2000 Tony Monroe


class Yacs():
    def __init__(self):
        self.wrap_len = 30
        self.yac_saying = 'Moooo!'

        self.eye_types = {
            'default': 'oo',
            'g': '!!',
            'x': 'XX',
            's': '**',
            't': '--',
            'w': 'OO',
            'y': '..',
            'h': '##'
        }
        self.eye_type = self.eye_types['default']


    def eyes(self, eye_type=None):
        if eye_type and eye_type in self.eye_types:
            self.eye_type = self.eye_types[eye_type]
        return self.eye_type


    def saying(self, saying=None):
        if saying:
            self.yac_saying = saying
        return self.yac_saying


    def wrap(self, wrap_chars=None):
        if wrap_chars:
            self.wrap_len = wrap_chars
        return self.wrap_len


    def thoughts(self):
        lines = []
        line_len = -1
        saying = ''
        max_allowed_len = self.wrap()
        max_length = 0

        for word in self.saying():
            if line_len + len(word) <= max_allowed_len:
                line_len += len(word) + 1
                saying = saying + ' ' + word
            else:
                lines.append({'length': line_len, 'saying': saying})
                line_len = len(word)
                saying = ' ' + word

            if max_length < line_len:
                max_length = line_len

        # have to catch the last line
        lines.append({'length': line_len, 'saying': saying})

        top_bot = '-' * (max_length + 4)
        thoughts = top_bot + '\n'
        for line in lines:
            buff = max_length - line['length']
            thoughts += '|' + line['saying'] + ' ' * buff + ' |\n'
        thoughts += top_bot

        return thoughts


    def the_yac(self):
        yac = '\n'.join([
            self.thoughts(),
            '    \   ^__^',
            '     \  (' + self.eyes() + ')\_______',
            '        (__)\       )\/\\',
            '            ||----w |',
            '            ||     ||'
        ])

        return yac
