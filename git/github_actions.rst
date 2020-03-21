.. title:: github actions

.. meta::
    :description:
        Справочная информация по github actions..
    :keywords:
        github actions

github actions
==============

.. code-block:: yaml

    # .github/workflows/task.yml


    # ---
    # коментарии
    # <img src="https://github.com/ilnurgi/testing-actions/workflows/action_name/badge.svg?branch=master">
    # ---

    name:  my-actions
    env:
        APPLICATION_NAME: "MyApplicationName"
        PACKAGE_NAME: "package-${{ github.sha }}"

    on:
        push:
            branches:
                - master

    jobs:
        my_testing:
            runs-on: ubuntu-last

            steps:
            - name: My printer
              run: echo "hello from testing"

            - name: clone repo
              run: actions/checkout@v1

            - name: second printer
              run: |
                echo "1"
                echo "2"
                echo "${{ env.APPLICATION_NAME }}"
                ls -la
                echo "${{ secrets.SECRET_KEY }}"

        my_deploying:
            runs-on: ubuntu-last
            needs: [my_testing]
            env:
                VAR1: "var1"

            steps:
            - name: My deploying
              run: echo "hello from deploying"
              env:
                VAR2: "var2"

            - name: My deploying2
              run: echo $VAR2
              env:
                VAR2: "var2"
