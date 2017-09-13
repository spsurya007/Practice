_DEPTH = 2


def _count(x, i, depth, indices, highest_value):
    """Count the sets of divisible numbers of a specific depth."""
    out = 0
    for m in xrange(1, int(highest_value / x) + 1):
        if x * m in indices:
            for j in indices[x * m]:
                if i < j:
                    if depth == _DEPTH:
                        out += 1
                    else:
                        out += _count(x * m, j, depth + 1,
                                      indices, highest_value)

    return out


def answer(l):
    indices = {}
    setdefault_ = indices.setdefault
    for i, x in enumerate(l):
        setdefault_(x, []).append(i)

    out = 0
    highest_value = max(l)
    for i, x in enumerate(l):
        out += _count(x, i, 1, indices, highest_value)

    return out
