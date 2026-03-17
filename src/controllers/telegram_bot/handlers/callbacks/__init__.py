from .agreement import get_agreement_agree_callback
from .cancel import get_cancel_message
from .delete_profile import get_delete_profile_confirm_callback
from .leagues_info import get_add_profile_callback, get_fast_statistic_callback
from .leagues_tutorials import get_fast_statistic_tutorial_callback

__all__ = [
    "get_add_profile_callback",
    "get_agreement_agree_callback",
    "get_delete_profile_confirm_callback",
    "get_fast_statistic_tutorial_callback",
    "get_fast_statistic_callback",
    "get_cancel_message",
]
