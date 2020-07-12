import os
from django.core.exceptions import ValidationError

def validate_is_glb(v):
    ext = os.path.splitext(v.name)[1]
    if not ext.lower() in ('.glb'):
        raise ValidationError("Only .glb file could be uploaded.")
