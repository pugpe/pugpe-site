from datetime import datetime

from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _


def check_required_fields_for_a_valid_event(event):
    """Checks event's required fields."""
    required_fields = {
        "title": str,
        "description": str,
        "start_date": datetime,
        "end_date": datetime,
    }

    for field in required_fields:
        field_value = getattr(event, field)
        field_type = required_fields[field]

        if isinstance(field_value, field_type):
            # Checks blank fields
            if field_type == str and len(field_value) == 0:
                raise ValidationError(_(f"`{field}` is required."))
        else:
            raise ValidationError(_(f"`{field}` is required."))
