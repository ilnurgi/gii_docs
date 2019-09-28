import os
import shutil
import sys

from io import StringIO
from multiprocessing import Pool
from time import time

from sphinx.cmd import build

base_dir = os.path.dirname(__file__)
build_html_dir = os.path.join(base_dir, '_build_html')
build_epub_dir = os.path.join(base_dir, '_build_epub')


def prepare_build_path():
    for path in (build_html_dir, build_epub_dir):
        if os.path.exists(path):
            print(path, 'exists, remove')
            # os.remove(build_dir)
            shutil.rmtree(path)
        else:
            os.makedirs(path)


def build_html(args):
    mode, build_dir, item = args

    print('start', mode, item)

    stdout = StringIO()
    stderr= StringIO()

    stdout_def = sys.stdout
    stderr_def = sys.stderr

    sys.stdout = stdout
    sys.stderr = stderr

    build.main(
        [
            '-c',
            base_dir,
            '-b',
            mode,
            os.path.join(base_dir, item),
            os.path.join(build_dir, item),
        ]
    )
    result = [stdout.getvalue()]
    result.append(stderr.getvalue())

    sys.stdout = stdout_def
    sys.stderr = stderr_def
    print('done', mode, item)

    return result


if __name__ == '__main__':
    prepare_build_path()
    modules = [
        'android',
        'arduino',
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
    jobs = [('html', build_html_dir, m) for m in modules]
    jobs.extend(('epub', build_epub_dir, m) for m in modules)
    result_jobs = Pool().map(build_html, jobs)

    r = []
    for result_job in result_jobs:
        for std in result_job:
            for line in std.split('\n'):
                if (
                        line.startswith('reading sources...') or
                        line.startswith('writing output...')
                ):
                    continue

                r.append(line)

    with open(os.path.join(base_dir, '{}.log'.format(int(time()))), 'w') as f:
        f.write('\n'.join(r))
