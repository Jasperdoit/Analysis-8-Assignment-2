import re
class security:
    def is_valid_username(username):
        # Regex pattern to validate username
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{7,11}$'
        return re.match(pattern, username) is not None

    def is_valid_password(password):
        # Regex pattern to validate password
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,30}$'
        return re.match(pattern, password) is not None