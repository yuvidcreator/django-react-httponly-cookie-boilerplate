# Django Backend API

# Django Djoser endpoints 
# Available endpoints
# Token based --> 
/api/token/
/api/token/refresh/
/api/token/verify/

# djoser --> /api/v1/auth/
/users/
/users/me/          (GET, PUT, PATCH)
/users/confirm/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/       (Token Based Authentication)
/token/logout/      (Token Based Authentication)
/jwt/create/        (JSON Web Token Authentication)
/jwt/refresh/       (JSON Web Token Authentication)
/jwt/verify/        (JSON Web Token Authentication)


/users/activation/{uid}/{token}
/users/resend_activation/{uid}/{token}


docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname



Bluedart way bill no - 20420299572



CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",    # env("CACHE_BACKEND")
        "LOCATION": "redis://127.0.0.1:6379/0",             # env("CACHE_LOCATION")
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",    # env("CACHE_LOCATION")
        },
    }
}

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "django-db"
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"