from allauth.account.adapter import DefaultAccountAdapter


class NoAuthMessageAdapter(DefaultAccountAdapter):
    """
    Suppresses django-allauth's built-in Django messages.
    Use when the project provides its own auth success/error messages.
    """

    def add_message(
        self,
        request,
        level,
        message_template=None,
        message_context=None,
        extra_tags="",
        message=None,
    ):
        return
