# A user can only attempt login 3 times within 60 seconds

# If exceeded → block user

# user_attempts = {
#   "username": [timestamps]
# }

def can_login(username, timestamp):
    """
    Return True if user is allowed to attempt login,
    False if rate-limited
    """
    # TODO
    