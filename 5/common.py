def react(a, b):
    lhs, ret = (a[-1], a[:-1]) if len(a) > 1 else (a, "")
    return ret if lhs != b and lhs.lower() == b.lower() else a + b
