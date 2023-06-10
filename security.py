import re
class security:
    def is_valid_username(username):
        """Validates the username for the following criteria:
        1. The username must start with an alphabet or underscore."""
        # Regex pattern to validate username
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{7,11}$'
        return re.match(pattern, username) is not None

    def is_valid_password(password):
        # Regex pattern to validate password
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-=\\`|\(\){}\[\]:;\'<>,\.\?/])[a-zA-Z\d~!@#$%&_\-=\\`|\(\){}\[\]:;\'<>,\.\?/]{12,30}$"
        return re.match(pattern, password) is not None