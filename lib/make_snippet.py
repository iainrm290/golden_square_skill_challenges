def make_snippet(string):
    snippet = string.split()
    snippet_to_return = " ".join(snippet[:5])
    if len(snippet) > 5:
        return snippet_to_return + "..."
    else:
        return snippet_to_return