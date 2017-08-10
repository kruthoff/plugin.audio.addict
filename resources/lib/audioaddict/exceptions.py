"""
    audioaddict.exceptions
    Simple exceptions specific to this addon.
"""


class AudioAddictException(Exception):
    pass


class AuthenticationError(AudioAddictException):
    pass


class EmptyCredentialsError(AudioAddictException):
    pass


class NoNetworksSelectedError(AudioAddictException):
    pass


class ListenKeyError(AudioAddictException):
    pass
