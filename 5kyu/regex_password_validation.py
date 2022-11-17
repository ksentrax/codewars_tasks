"""
Write regex that will validate a password to make sure it meets the following criteria:

- At least six characters long
- contains a lowercase letter
- contains an uppercase letter
- contains a digit
- only contains alphanumeric characters (note that '_' is not alphanumeric).
"""
import re

regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,}$"

# ^             begin word
# (?=.*[A-Z])   at least one uppercase letter
# (?=.*[a-z])   at least one lowercase letter
# (?=.*[0-9])   at least one number
# [A-Za-z\d]    only alphanumeric
# {6,}          at least 6 characters long
# $             end word
