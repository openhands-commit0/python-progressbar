from . import bar

def progressbar(*args, **kwargs):
    """Create and start a progress bar, then return an iterator.

    The context manager API is more convenient than this function since the
    progress bar is automatically cleared on exit, but not all implementations
    may support the context manager API.

    >>> progress = progressbar(range(100))
    >>> for i in progress:
    ...     pass
    """
    return bar.ProgressBar(*args, **kwargs)