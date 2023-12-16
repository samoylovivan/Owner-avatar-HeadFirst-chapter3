
def search4vowels(word):
    """Display any vowels found in asked-for word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
