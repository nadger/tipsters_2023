from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from tipsters.entry.views import entryview

urlpatterns = [
    path("entry/<int:pk>/", entryview.as_view(), name="entry"),
]
