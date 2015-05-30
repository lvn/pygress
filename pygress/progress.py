
import sys


class ProgressBar():
    def __init__(self, length=30, progress=0.0, progchar='#', emptychar='-',
                 show_percent=False, message=''):
        self.length = length
        self.progress = progress
        self.progchar = progchar
        self.emptychar = emptychar
        self.show_percent = show_percent
        self.message = message

    def set_progress(self, progress):
        self.progress = progress

    def add_progress(self, delta):
        self.progress += delta

    def subtract_progress(self, delta):
        self.progress -= delta

    def render(self):
        bar_len = min(int(self.progress * self.length), self.length)
        empty_len = self.length - bar_len
        sys.stdout.write('{} |'.format(self.message))
        sys.stdout.write(bar_len * self.progchar)
        sys.stdout.write(empty_len * self.emptychar)
        sys.stdout.write('| ')
        if self.show_percent:
            sys.stdout.write('{}%'.format(int(self.progress * 100)))
        sys.stdout.write('\r' if self.progress < 1.0 else '\n')
