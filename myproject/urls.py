from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', base , name='base'),
    path('mybase/', mybase , name='mybase'),
    path('home/', home , name='home'),
    path('skills/', skills , name='skills'),
    path('blog/', blog , name='blog'),
    path('experience/', experience , name='experience'),
    path('project/', project , name='project'),


    path('single/<int:id>', single , name='single'),
    path('single2/<int:id>', single2 , name='single2'),
    path('single3/<int:id>', single3 , name='single3'),
    path('single4/<int:id>', single4 , name='single4'),

    
    path('AddPhotograph1/', AddPhotograph1 , name='AddPhotograph1'),
    path('AddPhotograph2/', AddPhotograph2 , name='AddPhotograph2'),
    path('AddPhotograph3/', AddPhotograph3 , name='AddPhotograph3'),
    path('AddPhotograph4/', AddPhotograph4 , name='AddPhotograph4'),


    path('image_gallery/', image_gallery , name='image_gallery'),
    path('one_gelary/', one_gelary , name='one_gelary'),
    path('two_gelary/', two_gelary , name='two_gelary'),
    path('three_gelary/', three_gelary , name='three_gelary'),
    path('four_gelary/', four_gelary , name='four_gelary'),


    path('logoutpage/', logoutpage , name='logoutpage'),
    path('', loginpage , name='loginpage'),
    path('registerpage/', registerpage , name='registerpage'),
    path('password_change/', password_change , name='password_change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
