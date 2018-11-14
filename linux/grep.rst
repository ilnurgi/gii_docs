grep
====

.. code-block::sh

	# A-Z, a-z, 0-9
	grep "^[[:alnum:]]" ilnurgi.txt

	# A-Z, a-z
	grep "^[[:alpha:]]" ilnurgi.txt

	# A-Z
	grep "^[[:upper:]]" ilnurgi.txt

	# a-z
	grep "^[[:lower:]]" ilnurgi.txt

	# 0-9
	grep "^[[:digit:]]" ilnurgi.txt

	# 0-9, A-F, a-f
	grep "^[[:xdigit:]]" tecmint.txt

	# tab, space
	grep "^[[:blank:]]" ilnurgi.txt

	# tab, newline, vertical tab, form feed, carriage return, space
	grep "^[[:space:]]" ilnurgi.txt

	# [! ” # $ % & ‘ ( ) * + , – . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~. ]
	grep "^[[:punct:]]" ilnurgi.txt

	# 0-9, символы пунктуации
	grep "^[[:graph:]]" tecmint.txt

	# печатные символы
	grep "^[[:print:]]" tecmint.txt


.. code-block:: sh

	# вывод 2 линии до и после найденной строки
	grep -C 2 "remix" ilnurgi.txt

	# вывод 2 линии до найденной строки
	grep -A 2 "remix" ilnurgi.txt

	# вывод 2 линии после найденной строки
	grep -B 2 "remix" ilnurgi.txt

	# вывод количества найденных вхождений
	grep -c "remix" ilnurgi.txt

	# вывод номера строки, найденных вхождений
	grep -n "remix" ilnurgi.txt

	# рекурсинвый поиск 
	grep -r "remix" .

	# поиск по слову
	grep -w "remix" ilnurgi.txt



.. code-block:: sh

	grp -i "JayZ" | grep -vi "remix"
