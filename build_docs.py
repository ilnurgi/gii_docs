import os
import shutil
import sys

from argparse import ArgumentParser
from io import StringIO
from time import time
from multiprocessing import Pool

from sphinx.cmd import build

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# путь до папки, куда складываем сконвертированные файлы
BUILD_DIR_HTML = os.path.join(BASE_DIR, '_build_html')
BUILD_DIR_EPUB = os.path.join(BASE_DIR, '_build_epub')

# список папок, которые обрабатываем
DIR_NAMES = [
    'android',
    'arduino',
    'cplus',
    'css',
    'docker',
    'git',
    'html',
    'java',
    'js',
    'kotlin',
    'linux',
    'nginx',
    'puppet',
    'python',
    're',
    'sql',
    'svg',
]


def prepare_build_dir(build_dir: str, app_args: ArgumentParser):
    """функция подготовки папки для выгрузки
    """

    if app_args.clean and os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)


def build_html_parallel(args):
    """функция конвертации для указанной папки, которая запускается параллельно
    :param args: параметры сборки
    """

    mode, dir_name, build_dir = args

    print('start', mode, dir_name)

    stdout = StringIO()
    stderr = StringIO()

    stdout_def = sys.stdout
    stderr_def = sys.stderr

    sys.stdout = stdout
    sys.stderr = stderr

    build_params = [
        # укажем папку с конфигом по умолчанию
        '-c', BASE_DIR,
        # укажем формат конвертируемых данных
        '-b', mode,
        # укажем папку обработки
        os.path.join(BASE_DIR, dir_name),
        # укажем папку выгрузки
        os.path.join(build_dir, dir_name),
    ]

    build.main(build_params)

    sys.stdout = stdout_def
    sys.stderr = stderr_def

    print('done', mode, dir_name)

    # возвращаем результата
    return stdout.getvalue(), stderr.getvalue()


if __name__ == '__main__':

    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        '-c',
        '--clean',
        help='Полная конвертация, с удалением папки выгрузки',
        action='store_true',
        dest='clean',
    )

    arg_parser.add_argument(
        '-d',
        '--dirs',
        help='Конвертировать указанные папки, по умолчанию все',
        default='all',
        dest='process_dirs',
        nargs='*',
    )

    app_args = arg_parser.parse_args()

    prepare_build_dir(BUILD_DIR_HTML, app_args)
    prepare_build_dir(BUILD_DIR_EPUB, app_args)

    # создадим список аргументов для функции параллельной обработки        
    # сначала html
    jobs_args = [
        ('html', dir_name, BUILD_DIR_HTML) 
        for dir_name in DIR_NAMES
        if 'all' in app_args.process_dirs or dir_name in app_args.process_dirs
    ]
    # затем epub
    jobs_args.extend(        
        ('epub', dir_name, BUILD_DIR_EPUB) 
        for dir_name in DIR_NAMES
        if 'all' in app_args.process_dirs or dir_name in app_args.process_dirs
    )

    # создаем пулл и запускаем обработку всех параметров задач
    # jobs_result - сохраним все что вернут процессы обработки
    jobs_results = Pool().map(build_html_parallel, jobs_args)

    # тут мы сохраним результаты работы в плоский список
    jobs_result_list = []

    # соберем в плоский список результаты, для последующей записи в лог файл
    for job_result in jobs_results:

        # job_result - tupe, то что возвращает функция build_html_parallel
        # это stdout, stderr
        for std in job_result:
            for line in std.split('\n'):
                # отфильтруем лишние строки
                if (
                        line.startswith('reading sources...') or
                        line.startswith('writing output...')
                ):
                    continue

                jobs_result_list.append(line)

    current_time = int(time())
    with open(os.path.join(BASE_DIR, f'{current_time}.log'), 'w') as f:
        f.write('\n'.join(jobs_result_list))
