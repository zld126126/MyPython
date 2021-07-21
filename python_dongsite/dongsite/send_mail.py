import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'dongsite.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.dongtech.com的测试邮件',
        '您好,这是一封测试邮件',
        'dongtech_test@sina.com',
        ['9312085@qq.com'],
    )
