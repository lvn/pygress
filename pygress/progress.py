
import sys


class ProgressBar():
    def __init__(self, length=30, progress=0.0, progchar='#', emptychar='-',
                 show_percent=False, message='', use_stderr=True):
        self.length = length
        self.progress = progress
        self.progchar = progchar
        self.emptychar = emptychar
        self.show_percent = show_percent
        self.message = message
        self.out = sys.stderr if use_stderr else sys.stdout

    def set_progress(self, progress):
        self.progress = progress

    def add_progress(self, delta):
        self.progress += delta

    def subtract_progress(self, delta):
        self.progress -= delta

    def render(self):
        bar_len = min(int(self.progress * self.length), self.length)
        empty_len = self.length - bar_len
        self.out.write('{} |'.format(self.message))
        self.out.write(bar_len * self.progchar)
        self.out.write(empty_len * self.emptychar)
        self.out.write('| ')
        if self.show_percent:
            self.out.write('{}%'.format(int(self.progress * 100)))
        self.out.write('\r' if self.progress < 1.0 else '\n')
