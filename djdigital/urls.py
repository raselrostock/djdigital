from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as user_views
from courses import views as course_views
from .views import HomeView
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler400, handler403, handler404, handler500
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, CourseSitemap, InstructorSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'courses': CourseSitemap,
    'instructors': InstructorSitemap
}

urlpatterns = [
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('007/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomeView, name='home'),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('instructors/', include('instructors.urls', namespace='instructors')),
    path('profile/', user_views.ProfileView, name='profile'),
    path('register/', user_views.UserRegistrationView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('dashboard/', include('memberships.urls', namespace='memberships')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', include('search.urls', namespace='search')),
    path('faqs/', include('pages.urls', namespace='pages')),
    path('subscribe/', include('subscriptions.urls', namespace='subscriptions'))
]


handler404 = 'djdigital.views.not_found'
handler500 = 'djdigital.views.server_error'
handler403 = 'djdigital.views.permission_denied'
handler400 = 'djdigital.views.bad_request'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
