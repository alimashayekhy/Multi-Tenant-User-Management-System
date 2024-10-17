from django.urls import path
from .views import AdminTestView, TechnicianTestView, OperatorTestView, RegularUserTestView

urlpatterns = [
    path('admin/test/', AdminTestView.as_view(), name='admin_test'),
    path('technician/test/', TechnicianTestView.as_view(), name='technician_test'),
    path('operator/test/', OperatorTestView.as_view(), name='operator_test'),
    path('user/test/', RegularUserTestView.as_view(), name='user_test'),
]