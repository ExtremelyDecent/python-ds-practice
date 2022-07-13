def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    paren_count = 0

    for p in parens:
        if p == '(':
            paren_count += 1
        elif p == ')':
            paren_count -= 1
        if paren_count < 0:
            return False
    return paren_count == 0
