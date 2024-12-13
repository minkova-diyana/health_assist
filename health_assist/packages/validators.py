from django.core.exceptions import ValidationError


class FileSizeValidator:
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        if value.size > self.max_size_mb * 1024 * 1024:  # Convert MB to bytes
            raise ValidationError(f"File size must be less than {self.max_size_mb} MB.")
