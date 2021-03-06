from django.conf.urls.defaults   import patterns, include, url
from django.contrib              import admin
from django.views.generic.simple import redirect_to

from userena                     import views as userena_views

admin.autodiscover()

urlpatterns = patterns('forum.views',
    (r'^$',                                      'home'),
    (r'^reports/$',                              'reports'),
#   (r'^search/$',                               'search'),
    (r'^subscriptions/$',                        'subscriptions'),

#   Category
    (r'^category/add/$',                         'add'),
    (r'^category/(?P<category_id>\d+)/create/$', 'create'),
#   (r'^category/(?P<category_id>\d+)/merge/$',  'merge'),
    (r'^category/(?P<category_id>\d+)/$',        'category'),

#   Thread
    (r'^thread/(?P<thread_id>\d+)/reply/$',      'reply'),
    (r'^thread/js/$',                            'thread_js'),
    (r'^thread/(?P<thread_id>\d+)/lock/$',       'lock_thread'),
    (r'^thread/(?P<thread_id>\d+)/sticky/$',     'sticky_thread'),
    (r'^thread/(?P<thread_id>\d+)/merge/$',      'merge_thread'),
    (r'^thread/(?P<thread_id>\d+)/move/$',       'move_thread'),
    (r'^thread/(?P<thread_id>\d+)/moderate/$',   'moderate_thread'),
    (r'^thread/(\d+)/report/$',                  'report',
                                                 	 {'object_type': 'thread'}),
    (r'^thread/(\d+)/remove/$',                  'remove',
                                                     {'object_type': 'thread'}),
    (r'^thread/(?P<thread_id>\d+)/$',            'thread',
                                                     {'author_id': "Everyone"}),
	(r'^thread/(?P<thread_id>\d+)/author/(?P<author_id>\d+)/$', 'thread'),

#   Post
    (r'^post/(?P<post_id>\d+)/edit/$',           'edit'),
    (r'^post/(\d+)/report/$',                    'report',
                                                     {'object_type': 'post'}),
    (r'^post/(\d+)/remove/$',                    'remove',
                                                     {'object_type': 'post'}),
    (r'^post/(?P<post_id>\d+)/$',                'post'),

#   User
    (r'^user/js/$',                              'user_js'),
    (r'^user/(?P<user_id>\d+)/threads/$',        'user_content', 
                                                     {'object_type': 'thread'}),
    (r'^user/(?P<user_id>\d+)/posts/$',          'user_content',
                                                     {'object_type': 'post'}),
    (r'^user/(?P<user_id>\d+)/$',                'user'),

#   Accounts
#   (r'^login/$',                                'login'),
#   (r'^logout/$',                               'logout'), 
#   (r'^signup/$',                               'register'),
#	(r'^settings/$',                             'settings'),

    # Redirecting undesired URLs in the userena app to home page
    # and replacing them with such ones as "login" and "logout".
    #
    # <?Pdummy> is there to capture the argument that should not 
    # be passed to the url of redirect_to().
    #
    # Kinda hacky, but gets it done.
    (r'^accounts/login/$',                        userena_views.signin),
    (r'^accounts/logout/$',                      'logout'),
    (r'^accounts/settings/$',                    'settings'),

    url(r'^accounts/$',
        redirect_to, {'url': '/'}),

    url(r'^accounts/signin/$',
        redirect_to, {'url': '/accounts/login/'}),

    url(r'^accounts/signout/$',
        redirect_to, {'url': '/accounts/logout/'}),

    url(r'^accounts/page/(?P<dummy>[0-9]+)/$',
        redirect_to, {'url': '/'}),

    url(r'^accounts/(?P<dummy>(?!login|logout|signup)[\.\w]+)/edit/$',
        redirect_to, {'url': '/'}),

    url(r'^accounts/(?P<dummy>(?!login|logout|signup)[\.\w]+)/$',
        redirect_to, {'url': '/'}),
)

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^accounts/',  include('userena.urls')),
)