# Pygress
### by [Elvin Yung](https://github.com/elvinyung)
## Simple commandline progress bars in Python

### Install
It's on [PyPi](https://pypi.python.org/pypi/pygress)! Install it using `pip install pygress`.

Right now I've only tested this with Python 3.3.4.

### Quickstart
```python
from pygress import ProgressBar

progress_bar = ProgressBar()
task = SomethingThatTakesTime()
while True:
    progress_bar.set_progress(task.progress)
    progress_bar.render()
    if task.progress >= 1.0:
        break
```

By default, the progress bar looks something like this:
```
|#########---------------------|
```

### Methods
#### `set_progress(progress)`
Sets the progress on the bar. Should be a float between `0.0` and `1.0`.

#### `add_progress(delta)`
Adds some progress to the bar. Should be a float less than `1.0`.

#### `subtract_progress(delta)`
Subtracts some progress from the bar. Should be a float less than `1.0`.

#### `render`
Renders the progress bar to output. 

### Parameters
#### `length`
Sets the maximum length of the progress bar. Defaults to 30.

#### `progress`
Sets the initial progress. Defaults to 0.0.

#### `progchar`
Sets the character to show for the progressed part of the bar. Defaults to `#`.

#### `emptychar`
Sets the character to show for the yet to progress part of the bar. Defaults to `-`.

#### `show_percent`
Determines whether to show the percent to the right of the bar. Defaults to `False`.

If `True`, the progress bar looks like this: 
```
|#########---------------------| 30%
```

#### `message`
Sets the message to be shown to the left of the bar. Defaults to empty string.

If message is set, the progress bar looks like this (for an example of message as "`Loading...`"):
```
Loading... |#########---------------------|
```

#### `use_stderr`
If `True`, the progress bar is printed to stderr. If `False`, the progress bar is printed to stdout. Defaults to