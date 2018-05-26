# db_final
db_final

create database db_final;

python manage.py migrate

python manage.py runserver

https://github.com/leoleo30539/db_final_example

    path('', Home_views.home),  # new
    path('home/', Home_views.home),  # new
    path('admin/', admin.site.urls),
    path('login/', login_views.login),
    path('Annoucement/', Annoucement_views.anncs),
    path('events/', event_views.events),
    path('signup/', signup_views.signup)
