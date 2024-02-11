from itertools import combinations

def alternate(s):
    max_alt_len = 0
    charset = set(s)

    if len(charset) <= 1:
        return 0

    def is_alternative(string):
        odd = set(string[0::2])
        even = set(string[1::2])
        return len(odd) == len(even) == 1
    
    def remove_charset(charset, string):
        transdict = {c: '' for c in todelete}
        transobj = str.maketrans(transdict)
        return string.translate(transobj)

    for todelete in combinations(charset, len(charset) - 2):
        tmps = remove_charset(todelete, s)
        if is_alternative(tmps):
            max_alt_len = max(max_alt_len, len(tmps))
    
    return max_alt_len
    