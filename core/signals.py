"""
Authentication-related signal handlers.

This module centralises user-facing feedback messages triggered by
authentication events such as signup, login, and logout. Messages are
intentionally handled here (rather than via django-allauth defaults)
to ensure consistent UX copy across the application.
"""

from django.contrib import messages
from django.dispatch import receiver
from allauth.account.signals import (
    user_logged_in,
    user_logged_out,
    user_signed_up,
)


@receiver(user_signed_up)
def add_signup_message(request, user, **kwargs):
    """
    Display a welcome message when a user successfully registers.

    django-allauth automatically logs the user in after signup, which
    would normally also trigger the login signal. To prevent duplicate
    or misleading messages ("Welcome back"), a request-scoped flag is
    set here so the subsequent login handler can detect that this login
    originated from a signup event.
    """
    request._from_signup = True
    messages.success(request, f"Welcome to StudyStack, {user.get_username()}!")


@receiver(user_logged_in)
def add_login_message(request, user, **kwargs):
    """
    Display a welcome-back message when an existing user logs in.

    If the login was triggered as part of the signup flow, the message
    is suppressed to avoid conflicting feedback. This is detected via
    a request-scoped flag set by the signup signal handler.
    """
    if getattr(request, "_from_signup", False):
        return

    messages.success(request, f"Welcome back, {user.get_username()}.")


@receiver(user_logged_out)
def add_logout_message(request, user, **kwargs):
    """
    Display a confirmation message when a user logs out.

    This provides clear feedback that the logout action has completed
    successfully.
    """
    messages.info(request, "You have been logged out.")
