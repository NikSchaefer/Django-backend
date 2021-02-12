def validate(password, user=None, min_length=8):
    re_special_characters = r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if not any(char.isdigit() for char in password):
        return ('Password must contain at least %(min_length)d digit.') % {
                               'min_length': min_length}
    if not any(char.isalpha() for char in password):
        return ('Password must contain at least %(min_length)d letter.') % {
                               'min_length': min_length}
    if not any(char in re_special_characters for char in password):
        return ('Password must contain at least %(min_length)d special character.') % {
                               'min_length': min_length}
    return "Good"