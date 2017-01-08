from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Work, Hobby, StPlace, Course, Task, Organization
import datetime


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        d = list(map(int, datetime.datetime.now().isoformat()[0:10].split('-')))
        organizations = [{'name': 'ТД Альфа комплект', 'region': 'Москва', 'url': 'http://alfakomplekt.ru',
                          'activity': 'Проведение сертификационных испытаний электро-радио изделий'},
                         {'name': 'НТЦ ЮРИОН', 'region': 'Москва', 'url': 'http://www.yurion.ru',
                          'activity': 'Научно-технический центр «ЮРИОН» является известным российским разработчиком и'
                                      ' производителем цифровых систем передачи информации по радиоканалу.'},
                         {'name': 'ФГУП НПЦАП', 'region': 'Москва', 'url': 'http://www.npcap.ru',
                          'activity': 'Основной задачей коллектива является создание простых, надежных и '
                                      'оригинальных систем управления для ракет-носителей космических кораблей и'
                                      'межпланетных автоматических станции'},
                         {'name': 'НПО МИР', 'region': 'Омск', 'url': 'http://mir-omsk.ru',
                          'activity': 'НПО "МИР" оказывает полный комплекс услуг – разработка, производство,'
                                      ' проектирование, внедрение и сервис автоматизированных систем в электрических'
                                      ' сетях ресурсодобывающих, промышленных, транспортных и сетевых компаниях.'}]

        work_place = [{'organization': 'ТД Альфа комплект', 'D': 'Инженер - испытатель',
                       'time_st': datetime.date(2015, 7, 7), 'time_end': datetime.date(d[0], d[1], d[2]),
                       'ob': 'Проведение испытаний ЭРИ различной стпени интеграции'},
                      {'organization': 'НТЦ ЮРИОН', 'D': 'Инженер',
                       'time_st': datetime.date(2015, 3, 3), 'time_end': datetime.date(2015, 7, 6),
                       'ob': 'Разработка электрорадиоизделий, программирование микроконтроллеров'},
                      {'organization': 'ФГУП НПЦАП', 'D': 'Инженер 2 категории',
                       'time_st': datetime.date(2014, 8, 15), 'time_end': datetime.date(2015, 3, 2),
                       'ob': 'Разработка программного обоспечения для БЦВМ на языке Ассемблер'},
                      {'organization': 'НПО МИР', 'D': 'Техник',
                       'time_st': datetime.date(2014, 2, 4), 'time_end': datetime.date(2014, 6, 27),
                       'ob': 'Занимался разработкой пульта проверки интерфейсов CAN и RS - 232, программирование ARM'}]
        hobbies = [{'name': 'Python', 'url': '/static/mainapp/img/python.jpg'},
                   {'name': 'Электроника (ПЛИС, ARM)', 'url': '/static/mainapp/img/electronic.jpg'},
                   {'name': 'Кактусы', 'url': '/static/mainapp/img/cactus.jpg'},
                   {'name': 'Пауэрлифтинг', 'url': '/static/mainapp/img/lifting.jpg'}]
        studies = [{'name': 'Омский государственный технический университет', 'url': 'http://www.omgtu.ru',
                    'sp': 'Автоматизация технологических процессов и производств', 'Level': 'Специалист',
                    'dip': 'Практикум про программированнию ПЛИС на языке Verilog HDL',
                    'time_st': datetime.date(2009, 9, 1), 'time_end': datetime.date(2014, 6, 30)},
                   {'name': 'Омский государственный технический университет', 'url': 'http://www.omgtu.ru',
                    'sp': 'Курсы элитного образования', 'Level': '-', 'dip': '-',
                    'time_st': datetime.date(2009, 9, 15), 'time_end': datetime.date(2013, 5, 31)},
                   {'name': 'Московский технологический университет', 'url': 'https://www.mirea.ru',
                    'sp': 'Управление в технических системах', 'Level': 'Магистр',
                    'dip': 'Задача байесовской фильтрации информационных потоков в промышленных АСУ',
                    'time_st': datetime.date(2014, 10, 1), 'time_end': datetime.date(2016, 7, 15)}]
        curs_place = [{'org': 'Интуит',
                       'url': 'http://www.intuit.ru/verifydiplomas/100906267',
                       'sp': 'Программирование на Си ',
                       'Data': '2014'},
                      {'org': 'Специалист',
                       'url': 'http://www.specialist.ru',
                       'sp': 'Программирование на языке С (Си) ',
                       'Data': '2014'},
                      {'org': 'Специалист',
                       'url': 'http://www.specialist.ru',
                       'sp': 'Программирование на Visual C++ ',
                       'Data': '2014'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/71474',
                       'sp': 'GIt. Быстрый старт. Инструмент командной разработки',
                       'Data': '2016'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/47681',
                       'sp': 'Курс HTML/CSS. Основы создания сайтов',
                       'Data': '2016'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/64351',
                       'sp': 'Курс JavaScript. Уровень 1. Интерактивные веб-приложения',
                       'Data': '2016'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/67233',
                       'sp': 'Успешно прошел тестирование по Python. Средний уровень',
                       'Data': '2016'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/54072',
                       'sp': 'Окончил курс Python. Уровень1. Основы языка и разработки веб-приложений',
                       'Data': '2016'},
                      {'org': 'geekbrains',
                       'url': 'https://geekbrains.ru/certificates/100489',
                       'sp': 'Видео-курс: основы баз данных. Язык SQL',
                       'Data': '2016'}]
        tasks = [{'url_pi': 'https://static.checkio.org/media/logos/task/middle/c-islands-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/calculate-islands/',
                  'url_sov': '/static/mainapp/file/island.txt',
                  'category': 'graf'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/open-labyrinth-new-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/open-labyrinth/',
                  'url_sov': '/static/mainapp/file/labirint.txt',
                  'category': 'graf'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/disposable-teleports-new-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/disposable-teleports/',
                  'url_sov': '/static/mainapp/file/teleport.txt',
                  'category': 'graf'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/express-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/express-delivery/',
                  'url_sov': '/static/mainapp/file/box.txt',
                  'category': 'graf'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/pd-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/probably-dice/',
                  'url_sov': '/static/mainapp/file/dinamic.txt',
                  'category': 'din'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/pb-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/box-probability/',
                  'url_sov': '/static/mainapp/file/box-probability.txt',
                  'category': 'din'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/four-color-on.png',
                  'url_text': 'https://py.checkio.org/mission/color-map/',
                  'url_sov': '/static/mainapp/file/color-map.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/solution_of_enything_enabled.png',
                  'url_text': 'https://py.checkio.org/mission/solution-for-anything/',
                  'url_sov': '/static/mainapp/file/magic.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/rotate-hole-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/rotate-hole/',
                  'url_sov': '/static/mainapp/file/rotate-hole.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/network-attack-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/network-attack/',
                  'url_sov': '/static/mainapp/file/network-attack.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/broken-clock-on.png',
                  'url_text': 'https://py.checkio.org/mission/broken-clock/',
                  'url_sov': '/static/mainapp/file/broken-clock.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/enabled_29.png',
                  'url_text': 'https://py.checkio.org/mission/cipher-map2/',
                  'url_sov': '/static/mainapp/file/cipher-map2.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/enabled_25.png',
                  'url_text': 'https://py.checkio.org/mission/painting-wall/',
                  'url_sov': '/static/mainapp/file/painting-wall.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/ghosts-age-enabled.png',
                  'url_text': 'https://py.checkio.org/mission/ghosts-age/',
                  'url_sov': '/static/mainapp/file/ghosts-age.txt',
                  'category': 'another'},
                 {'url_pi': 'https://static.checkio.org/media/logos/task/middle/amsco-on.png',
                  'url_text': 'https://py.checkio.org/mission/amsco-cipher/',
                  'url_sov': '/static/mainapp/file/amsco-cipher.txt',
                  'category': 'another'}]
        Organization.objects.all().delete()
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()
        Work.objects.all().delete()
        for work in work_place:
            org_name = work["organization"]
            organization = Organization.objects.get(name=org_name)
            work['organization'] = organization
            work = Work(**work)
            work.save()
        Hobby.objects.all().delete()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()
        StPlace.objects.all().delete()
        for study in studies:
            study = StPlace(**study)
            study.save()
        Course.objects.all().delete()
        for curs in curs_place:
            curs = Course(**curs)
            curs.save()
        Task.objects.all().delete()
        for task in tasks:
            task = Task(**task)
            task.save()

