def vector_affinity(a, b):
    max_length = max(len(a), len(b))
    if max_length == 0:
        return 1.0
    min_length = min(len(a), len(b))
    matches = sum(1 for i in range(min_length) if a[i] == b[i])
    return matches / max_length
