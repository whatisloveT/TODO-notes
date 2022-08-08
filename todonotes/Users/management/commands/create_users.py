from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from Users.models import CustomUser


class Command(BaseCommand):
    help = 'Создает случайных пользователей'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Указывает сколько пользователей необходимо создать')

    def handle(self, *args, **kwargs):
        total = int(kwargs['total']) - 1
        CustomUser.objects.create_superuser(username=get_random_string(7),
                                            email='admin@' + get_random_string(5) + '.com',
                                            password='0987654321')
        for i in range(total):
            CustomUser.objects.create_user(username=get_random_string(7), email='', password='1234567890')
