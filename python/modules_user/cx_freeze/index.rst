.. title:: cx_freeze

.. meta::
    :description:
        Описание python модуля cx_freeze
    :keywords:
        python cx_freeze

cx_freeze
=========

.. code-block:: sh

    pip install cx_freeze

.. code-block:: py

    from cx_Freeze import setup, Executable

    executbles = [
        Executable(
            'example.py',
            targetName='hello_world.exe',
            base='Win32GUI',
            icon='example.ico',
        )
    ]

    includes = ['json']

    include_files = [
        'data.txt',
        'readme.txt',
        ('documentation.txt', 'doc/doc.txt'),
    ]

    excludes = ['unicodedata', 'logging', 'unittest', 'email']

    zip_include_packages = ['collections', 'encodings', 'emportlib']

    options = {
        'build_exe: {
            'includes': includes,
            'include_files': include_files,
            'excludes': excludes,
            'zip_include_packages': zip_include_packages,
            'build_exe': 'build_windows',
        }
    }

    setup(
        name='hello_world',
        version='0.0.1',
        description='description',
        executbles=executbles,
        options=options,
    )

.. code-block:: sh

    python setup.py build
