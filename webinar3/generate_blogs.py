import logging
import random
import string

logger = logging.getLogger(__name__)
if __name__ == "__main__":
    import os
    import sys

    import django

    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), "../")))
    logger.info(sys.path)
    print(sys.path)
    os.environ["DJANGO_SETTINGS_MODULE"] = "webinar3.settings"
    django.setup()
    from blog.models import Blog, Category


def generate_random_str(length: int) -> string:
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(10)])


def generate_blog():
    category, _ = Category.objects.get_or_create(name='Самый первый блог')
    blog_list = []
    for _ in range(100):
        blog_list.append(Blog(name='Блог номер %s' % generate_random_str(10),
                              slug=generate_random_str(20),
                              text=generate_random_str(200),
                              category=category)) 
        print('blog')
    Blog.objects.bulk_create(blog_list)


if __name__ == '__main__':
    generate_blog()



