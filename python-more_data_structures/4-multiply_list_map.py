def best_score(a_dictionary):
    return None if not a_dictionary else next(map(lambda k: k[1], sorted(map(lambda kv: (kv[1], kv[0]), a_dictionary.items()), reverse=True)))