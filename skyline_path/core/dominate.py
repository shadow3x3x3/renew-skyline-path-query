"""
Skyline Status need to be import.
"""
from . import SkylineStatus

class DominatingException(Exception):
    """
    Exception for Dominating
    """
    def __init__(self, cause, message):
        super().__init__(self, cause, message)
        self.cause = cause
        self.message = message

    def __str__(self):
        return self.cause + ':' + self.message


def dominate_check(attrs_1, attrs_2):
    """
    This is skyline query core method that is for
    dominating compare.
    """
    if len(attrs_1) is not len(attrs_2):
        raise DominatingException("lengths not match",
                                  len(attrs_1) +
                                  " is not match " +
                                  len(attrs_2))

    check_flag = len(attrs_1)
    flag = 0
    for i, attr in enumerate(attrs_1):
        if attr > attrs_2[i]:
            flag += 1
        elif attr < attrs_2[i]:
            flag -= 1
        else:
            check_flag -= 1

    if flag is check_flag:
        return SkylineStatus.BE_DOMINATED
    elif flag is 0 - check_flag:
        return SkylineStatus.DOMINATE
    return SkylineStatus.NON_DOMINATE
