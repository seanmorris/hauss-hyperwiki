from django_hosts import patterns, host

host_patterns = patterns(
  '',
    host(r'', 'mysite.urls', name=' '),
    host(r'blog', 'blog.urls', name='blog'),
)