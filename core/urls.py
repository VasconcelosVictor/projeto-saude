from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login , name='login' ),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('register-patients/', register_patients, name='register-patients'),
    path('edit-patients/<int:id>/', register_patients, name='edit-patients'),
    path('delete_patient/<int:id>', delete_patient, name='delete-patient'),
    path('register-assessment/<int:patient_id>/', submit_assessment, name='register-assessment'),
    path('edit-assessment/<int:id>/<int:patient_id>/', submit_assessment, name='edit-assessment'),
    path('assessment_list/', assessment_list, name='assessment_list'),
    path('delete_assessment/<int:id>', delete_assessment, name='delete-assessment'),



]