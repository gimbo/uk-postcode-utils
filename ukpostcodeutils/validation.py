from functools import partial
import re

# See http://www.govtalk.gov.uk/gdsc/html/noframes/PostCode-2-1-Release.htm

PARTS = {
    'fst': 'ABCDEFGHIJKLMNOPRSTUWYZ',
    'sec': 'ABCDEFGHKLMNOPQRSTUVWXY',
    'thd': 'ABCDEFGHJKMNPRSTUVWXY',
    'fth': 'ABEHMNPRVWXY',
    'inward': 'ABDEFGHJLNPQRSTUWXYZ',
}

FULL_MATCH_REGEX = re.compile('|'.join([r.format(**PARTS) for r in (
    '^[{fst}][1-9]\d[{inward}][{inward}]$',
    '^[{fst}][1-9]\d\d[{inward}][{inward}]$',
    '^[{fst}][{sec}]\d\d[{inward}][{inward}]$',
    '^[{fst}][{sec}][1-9]\d\d[{inward}][{inward}]$',
    '^[{fst}][1-9][{thd}]\d[{inward}][{inward}]$',
    '^[{fst}][{sec}][1-9][{fth}]\d[{inward}][{inward}]$',
)]))

PARTIAL_MATCH_REGEX = re.compile('|'.join([r.format(**PARTS) for r in (
    '^[{fst}][1-9]$',
    '^[{fst}][1-9]\d$',
    '^[{fst}][{sec}]\d$',
    '^[{fst}][{sec}][1-9]\d$',
    '^[{fst}][1-9][{thd}]$',
    '^[{fst}][{sec}][1-9][{fth}]$',
)]))

del PARTS


def _match_postcode(regex, pc, extra_postcodes=()):
    if pc in extra_postcodes:
        return True
    return regex.match(pc) is not None


is_valid_postcode = partial(_match_postcode, FULL_MATCH_REGEX)
is_valid_partial_postcode = partial(_match_postcode, PARTIAL_MATCH_REGEX)
