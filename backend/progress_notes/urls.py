from django.urls import path
from . import views as P

urlpatterns = [
    path('get/', P.ProgressNoteView.as_view(), name='get_note_s'),
    path('save/', P.ProgressNoteSave.as_view(), name='save_note'),
    path('referral/', P.ProgressNoteViewByReferral.as_view(), name='referral_note_s'),
]
