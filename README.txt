========
Post Box
========

This post box is a "postal service" that helps users send feedback messages to their team members or colleagues. The feedback entered is stored anonymously. The "post master" sorts out and collates the messages and sends them to the intended recipients.


Quick start
-----------

1. Add "PostBox" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'PostBox',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^PostBox/', include('PostBox.urls'), namespace='PostBox')),
   Or you can include it in the index page of the website itself like this::
      url(r'^$', include('PostBox.urls', namespace='PostBox')),
