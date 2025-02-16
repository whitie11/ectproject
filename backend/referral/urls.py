from django.urls import path
from . import views as R

urlpatterns = [
    path('get/', R.ReferralView.as_view(), name='get_patient_s'),
    path('save/', R.ReferralSave.as_view(), name='save_referral'),
]
