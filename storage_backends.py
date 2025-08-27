from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static"  # This matches AWS_LOCATION
    default_acl = "public-read"
