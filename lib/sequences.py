def remove_duplicates(sequence):
    seen = set()
    result = []

    for i in sequence:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result
