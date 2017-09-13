def lin(seq):
    seq = tuple(seq)
    cache = {}
    def inner(seq):
        if len(seq) == 1:
            return seq

        ret = cache.get(seq, None)
        if ret is not None:
            return ret

        longest = (seq[-1],)
        for index in range(1, len(seq)):
            till_index = inner(seq[:index])
            till_index += (seq[-1],) if till_index[-1] < seq[-1] else ()
            longest = max(longest, till_index, key=len)
        cache[seq] = longest
        return longest
    return inner(seq)
a=lin('abcbcbcd')
print(a)