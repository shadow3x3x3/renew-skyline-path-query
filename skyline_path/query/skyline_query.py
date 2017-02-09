from skyline_path.core import SkylineStatus
from skyline_path.core.dominate import dominate_check

def skyline_query(s):
    skylines = {}
    for q in list(s):
        _check(skylines, s, q)
    return skylines

def _check(skylines, s, q):
    for c in list(s):
        if q == c:
            continue
        else:
            if dominate_check(s[q], s[c]) == SkylineStatus.BE_DOMINATED:
                return
    skylines[q] = s[q]

