

from django.urls import path
from . import views as P

urlpatterns = [
    path('get/', P.PatientView.as_view(), name='get_patient_s'),
    path('save/', P.PatientSave.as_view(), name='save_patient'),
    path('search/', P.PatientSearch.as_view(), name='save_patient'),
]
