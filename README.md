# nonprofit-api
Boiler Plate for Djnago

# REVIEWLIN

## Build

- `sudo apt install python3-venv`
- `python3 -m venv name_of_virtual_environment`
- `source name_of_virtual_environment/bin/activate`
- `Pip install -r requirements.txt`
- `python manage.py createsuperuser` 
- `python manage.py runserver `




## Change Database Character-set to utf-8 for globalization
- `ALTER TABLE table_name CONVERT TO CHARACTER SET utf8;`

## Resources

- [Customizing rest-auth serializers](https://django-rest-auth.readthedocs.io/en/latest/configuration.html)
- [Adding rest-auth custom field to user](https://github.com/pennersr/django-allauth/blob/master/allauth/account/adapter.py#L227)
- [Customizing rest-auth user save adapter](https://stackoverflow.com/questions/37841612/django-rest-auth-custom-registration-fails-to-save-extra-fields)
- [Customizing Django Admin](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/two_admin.html)
- [Creating user profile](https://django-rest-auth.readthedocs.io/en/latest/faq.html)
- [Subscription Payment in Korea](https://docs.iamport.kr/implementation/subscription#extract-card)
- [Setting CORS](https://www.techiediaries.com/django-cors/)
- [HTTPS on Django](https://rickchristianson.wordpress.com/2013/10/31/getting-a-django-app-to-use-https-on-aws-elastic-beanstalk/)
- [AWS Official - HTTPS on Django ElasticBeanstalk Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html)
- [Stack Overflow Solution - HTTPS Redirection](https://stackoverflow.com/questions/14693852/how-to-force-https-on-elastic-beanstalk)
- [Django Python WSGI Pass Authorization](https://stackoverflow.com/questions/22279301/authorization-credentials-stripped-django-elastic-beanstalk-oauth)
- [Django Admin Drag & Drop Sortable](https://github.com/jrief/django-admin-sortable2)
- [Django Admin WYIWYG](https://github.com/django-ckeditor/django-ckeditor)
- [Django Elastic Beanstalk with External RDS](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)


- https://docs.python.org/2/library/uuid.html
- https://docs.iamport.kr/implementation/subscription#request-schedule-2
- https://api.iamport.kr/#/
- https://admin.iamport.kr/payments
- https://stackoverflow.com/questions/34325812/python-add-days-in-epoch-time
- https://www.django-rest-framework.org/api-guide/generic-views/
- [Overriding Reset Password Email](https://stackoverflow.com/questions/34897834/how-to-customize-django-rest-auth-password-reset-email-content-template/52111127#52111127)




## Visual Code essentials 
- Alphabetical Sorter 
