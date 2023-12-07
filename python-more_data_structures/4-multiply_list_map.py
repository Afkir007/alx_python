def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = max(map(lambda k: (a_dictionary[k], k), a_dictionary))[1]
    return max_key