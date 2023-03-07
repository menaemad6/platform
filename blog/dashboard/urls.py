import core.views
from django.urls import path



urlpatterns = [
    path('dashboard', core.views.dashboard, name='dashboard-page'),
    path('dashboard/<slug:slug>' , core.views.dashboard_lesson , name="lesson-page"),

    path('delete-lesson', core.views.delete_lesson, name='dashboard-delete-lesson'),

    path('dashboard-edit-student', core.views.dashboard_profiles, name='dashboard-edit-student'),

    path('inbox', core.views.inbox, name='inbox'),
    path('wallet/statement', core.views.account_activity, name='account-activity'),
    path('wallet/payments', core.views.account_payment, name='account-payment'),




    path('wallet/code-charge/request', core.views.code_charge, name='code-recharge'),
    path('lesson-code-charge', core.views.lesson_code_charge, name='code-recharge'),
    path('wallet/code-charge', core.views.charge_wallet_code, name='wallet-code-recharge'),
    path('wallet/code-charge', core.views.charge_wallet_code, name='wallet-code-recharge'),
    path('wallet/recharge', core.views.wallet_recharge, name='wallet-recharge'),
    path('wallet/requests', core.views.wallet_requests, name='wallet-requests'),
    # path('wallet/code-valid', core.views.wallet_requests, name='wallet-requests'),
    # path('wallet/code-invalid', core.views.wallet_requests, name='wallet-requests'),

]