c++
===

.. toctree::
    :maxdepth: 1

    var_types


Оконная процедура
-----------------

.. code-block:: cpp

    LRESULT CALLBACK FUNC_NAME(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
    {
        switch (uMsg)
        {
            case WM_COMAND:            
        }
    }


* LRESULT - LONG, возвращаемое оконной функции
* CALLBACK - спецификатор, который указывает на функцию обратного вызова
* hWnd — дескриптор окна, которому адресовано сообщение
* uMsg — код сообщения, описаны в winuser.h
    * WM_ - оконные сообщения
    * BT_ - кнопки
    * EM_ - текстовые поля
    * LB_ - списки
    * WM_ACTIVATE
    * WM_COMMAND
    * WM_CREATE
    * WM_DESTROY
    * WM_MOVE
    * WM_PAINT
    * WM_SETTINGCHANGE
    * WM_SIZE
    * WM_QUITE

* wParam и lParam — параметры сообщения

MessageBox()
------------

.. cpp:function:: int MessageBox(HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, UINT uType)

    * hWnd - идентифицирует окно владельца блока сообщений, которым оно было создано. 

        Если этот параметр имеет значение ПУСТО (NULL), у блока сообщения нет окна владельца.

    * lpText - указывает на строку с символом нуля в конце, содержащую сообщение, которое должно быть отражено на экране.

    * lpCaption - указывает на строку с символом нуля в конце, используемую для заголовка диалогового окна. 

        Если этот параметр значение ПУСТО (NULL), то по умолчанию используется заголовок Ошибка (Error).

    * uType - определяет установку битов флажков, которые обуславливают содержание и поведение диалогового окна. 

        * MB_ABORTRETRYIGNORE - Окно сообщение содержит три командных кнопки: Прервать (Abort), Повторить (Retry) и Проигнорировать (Ignore).
        * MB_APPLMODAL - Пользователь должен ответить окну сообщений перед продолжением работы в окне, которое идентифицировано параметром hWnd. Однако, пользователь может перемещаться в окнах других прикладных программ и работать в этих окнах.В зависимости от иерархии окон в прикладной программе, пользователь может получить возможность, чтобы перемещаться в другие окна в пределах прикладной программы. Все дочерние окна родителя окна сообщений автоматически блокируются, однако выскакивающие окна - нет.MB_APPLMODAL - значение по умолчанию, если не определен флажок, ни MB_SYSTEMMODAL, ни MB_TASKMODAL.
        * MB_CANCELTRYCONTINUE
        * MB_DEFAULT_DESKTOP_ONLY - Рабочий стол, в настоящее время принимающий ввод, должен быть заданным по умолчанию рабочим столом; иначе, функция не выполняет задачу. Заданный по умолчанию рабочий стол - первая запущенная прикладная программа, после того, как пользователь вошел в систему.
        * MB_DEFBUTTON1 - Первая кнопка - основная кнопка. MB_DEFBUTTON1 - значение по умолчанию, если не определена кнопка MB_DEFBUTTON2, MB_DEFBUTTON3 или MB_DEFBUTTON4.
        * MB_DEFBUTTON2 - Вторая кнопка - основная кнопка.
        * MB_DEFBUTTON3 - Третья кнопка - основная кнопка.
        * MB_DEFBUTTON4 - Четвертая кнопка - основная кнопка.
        * MB_HELP - Прибавляет кнопку Справка (Help) в окно сообщений. Выбор кнопки Help или нажатие F1 генерирует событие появления Справки.
        * MB_ICONEXCLAMATION, MB_ICONWARNING - В окне сообщений появляется пиктограмма восклицательного знака.
        * MB_ICONINFORMATION, MB_ICONASTERISK - В окне сообщений появляется пиктограмма, состоящая из символа i нижнего регистра в круге.
        * MB_ICONQUESTION - В окне сообщений появляется пиктограмма в виде знака вопроса.
        * MB_ICONSTOP, MB_ICONERROR, MB_ICONHAND - В окне сообщений появляется пиктограмма в виде стоп-сигнала.
        * MB_OK - Окно сообщение содержит одну командную кнопку: OK. Это по умолчанию.
        * MB_OKCANCEL - Окно сообщение содержит две командных кнопки: OK и Отменить (Cancel).
        * MB_RETRYCANCEL - Окно сообщение содержит две командных кнопки: Повторить (Retry) и Отменить (Cancel).
        * MB_RIGHT - Выравнивание текста справа.
        * MB_RTLREADING - Отображает на экране сообщение и текст заголовка с использованием порядка зеркального отображения для Еврейских и Арабских систем письменности.
        * MB_SERVICE_NOTIFICATION
        * MB_SETFOREGROUND - Окно сообщений становится приоритетным окном. Внутри Windows для окна сообщений вызывает функцию SetForegroundWindow.
        * MB_SYSTEMMODAL - То же самое, что и MB_APPLMODAL за исключением того, что окно сообщений имеет стиль WS_EX_TOPMOST. Используйте системно - модальные окна сообщений, чтобы уведомлять пользователя о серьезных, потенциально опасных ошибках, которые требуют немедленного внимания (например, запуск программы при нехватке памяти). Этот флажок не имеет никакого влияния на способность пользователя взаимодействовать с другими окнами, а не те, которые связаны с hWnd.
        * MB_TASKMODAL - То же самое, что и MB_APPLMODAL за исключением того, что все окна верхнего уровня, принадлежащие текущей задаче, заблокированы, если параметр hWnd имеет значение ПУСТО (NULL). Используйте этот флажок, когда вызывающая прикладная программа или библиотека не имеют доступного дескриптора окна, но все еще должны сохранять вводимые данные для других окон в текущей прикладной программе без приостановки работы других прикладных программ.
        * MB_TOPMOST - Окно сообщений создается со стилем окна WS_EX_TOPMOST.
        * MB_YESNO - Окно сообщение содержит две командных кнопки: Да (Yes) и Нет (No).
        * MB_YESNOCANCEL - Окно сообщение содержит три командных кнопки: Да (Yes), Нет (No) и Отменить (Cancel).

    Возвращаемые значения

        * IDABORT - Была выбрана кнопка Прервать (Abort).
        * IDCANCEL - Была выбрана кнопка Отменить (Cancel).
        * IDCONTINUE
        * IDIGNORE - Была выбрана кнопка Игнорировать (Ignore).
        * IDNO - Была выбрана кнопка Нет (No).
        * IDOK - Была выбрана кнопка OK.
        * IDRETRY - Была выбрана кнопка Повторить (Retry).
        * IDTRYAGAIN
        * IDYES - Была выбрана кнопка Да (Ye).

    .. code-block:: cpp

        int msgBoxId = MessageBox(NULL, L"Hello World", L"Hello CAPTION", MB_OK);

    .. code-block:: cpp

         int msgboxID = MessageBox(
            NULL,
            (LPCWSTR)L"Resource not available\nDo you want to try again?",
            (LPCWSTR)L"Account Details",
            MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2
        );

        switch (msgboxID)
        {
        case IDCANCEL:
            // TODO: add code
            break;
        case IDTRYAGAIN:
            // TODO: add code
            break;
        case IDCONTINUE:
            // TODO: add code
            break;
        }

WinMain()
---------

.. cpp:function:: WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)

    С этой функции начинается работы приложения.

    * hInstance - дескриптор, который Windows присваивает запущенному приложению.
    
    * hPrevInstance — в Win32 этот параметр не используется и поэтому всегда принимает нулевое значение.
 
    * lpCmdLine — указатель на строку, в которую копируются аргументы приложения, если оно запущено в режиме командной строки. 

    * nCmdShow — целое значение, которое может быть передано функции ShowWindow. 

    .. code-block:: cpp

        int WINAPI WinMain(
            HINSTANCE hInstance,
            HINSTANCE hPrevInstance,
            LPSTR lpCmdLine,
            int nCmdShow
        )
        {
            HWND hMainWnd;

            char szClassName[] = "MyClass";
            MSG msg;
            WNDCLASSEX wc;

            // заполняем структуру класса окна
            
            // UINT, размер данной структуры
            wc.cbSize = sizeof(wc);
            // UINT, стиль класса окна
            wc.style = CS_HREDRAW | CS_VREDRAW;
            // WNDPROC, указатель на оконную функцию
            wc.lpfnWndProc = WndProc; 
            // int, число дополнительных байтов, которые должны быть распределены в конце структуры класса
            wc.cbClsExtra = 0;
            // int, число доп. байтов, которые должны быть распределены вслед за экземпляром окна
            wc.cbWndExtra = 0;
            // HINSTANCE, дескриптор экземпляра приложения, в котором находится оконная процедура для этого класса
            wc.hInstance = hInstance;
            // HICON, дескриптор пиктограммы            
            wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
            // HCURSOR, дескриптор курсора
            wc.hCursor = LoadCursor(NULL, IDC_ARROW);
            // HBRUSH, дескриптор кисти, используемый для закраски фона
            wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
            // LPCTSTR, указатель на строку, содержащую имя меню
            wc.lpszMenuName = NULL;
            // LPCTSTR, указатель на строку, содержащую имя класса окна
            wc.lpszClassName = szClassName;
            // HICON, дескриптор малой пиктграммы
            wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

            // регистрируем класс окна
            if (!RegisterClassEx(&wc)) {
                MessageBox(NULL, "Cannot register class", "Error", MB_OK);
                return 0;
            }

            // создаем основное окно приложения
            hMainWnd = CreateWindow(
                szClassName, 
                "A Hello Application", 
                WS_OVERLAPPEDWINDOW,
                CW_USEDEFAULT, 
                0, 
                CW_USEDEFAULT, 
                0,
                (HWND)NULL, 
                (HMENU)NULL,
                (HINSTANCE)hInstance, 
                NULL
            );

            if (!hMainWnd) {
                MessageBox(NULL, "Cannot create main window", "Error", MB_OK);
                return 0;
            };

            // показываем окно
            ShowWindow(hMainWnd, nCmdShow);
            
            // UpdateWindow(hMainWnd);
            
            // цикл обработки сообщений
            while (GetMessage(&msg, NULL, 0, 0)) {
                TranslateMessage(&msg);
                DispatchMessage(&msg);
            }
            return msg.wParam;
        }


WindProc()
----------

.. cpp:function:: WindProc()

    Оконная цункция обработки собтиый окна приложения.

    .. code-block:: cpp

        LPRESULT CALLBACK WindProc(
            HWND hWnd,
            UINT uMsg,
            WPARAM wParam,
            LPARAM lParam
        )
        {
            HDC hDC;
            PAINTSTRUCT ps;
            RECT rect;
            switch (uMsg)
            {
                case WM_PAINT:
                    hDC = BeginPaint(hWnd, &ps);
                    GetClientRect(hWnd, &rect);
                    DrawText(
                        hDC, 
                        "Hello, World!", 
                        -1, 
                        &rect,
                        DT_SINGLELINE | DT_CENTER | DT_VCENTER 
                    );
                    EndPaint(hWnd, &ps);
                    break;
                case WM_CLOSE:
                    DestroyWindow(hWnd);
                    break;
                case WM_DESTROY:
                    PostQuitMessage(0);
                    break;
                default:
                    return DefWindowProc(hWnd, uMsg, wParam, lParam);
            }
            return 0;
        }


WNDCLASSEX
----------

.. cpp:struct:: WNDCLASSEX

    .. cpp:member:: UINT cbSize

        размер данной структуры

        .. code-block:: cpp

            wc.cbSize = sizeof(wc);


    .. cpp:member:: UINT style

        стиль класса окна

        * CS_GLOBALCLASS - класс, доступный всем приложениям
        * CS_HREDRAW - перерисовывает все окно, если изменен размер по горизонтали
        * CS_NOCLOSE - запретить команду CLOSE, в системном меню
        * CS_OWNDC - выделить уникальный контекст устройства для каждого окна
        * CS_VREDRAW - gththbcjdsdftn dct jryj? tckb bpvtyty hfpvth gj dthnbrfkb
        
        .. code-block:: cpp

            wc.style = CS_HREDRAW | CS_VREDRAW;


    .. cpp:member:: WNDPROC lpfnWndProc

        указатель на оконную функцию

        .. code-block:: cpp

            wc.lpfnWndProc = WndProc; 


    .. cpp:member:: int cbClsExtra

        число дополнительных байтов, которые должны быть распределены в конце структуры класса

        .. code-block:: cpp

            wc.cbClsExtra = 0;


    .. cpp:member:: int cbWndExtra

        число доп. байтов, которые должны быть распределены вслед за экземпляром окна

        .. code-block:: cpp

            wc.cbWndExtra = 0;


    .. cpp:member:: HINSTANCE hInstance

        дескриптор экземпляра приложения, в котором находится оконная процедура для этого класса

        .. code-block:: cpp

            wc.hInstance = hInstance;


    .. cpp:member:: HICON hIcon

        дескриптор пиктограммы

        .. code-block:: cpp

            wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);


    .. cpp:member:: HCURSOR hCursor

        дескриптор курсора

        .. code-block:: cpp

            wc.hCursor = LoadCursor(NULL, IDC_ARROW);


    .. cpp:member:: HBRUSH hbrBackground

        дескриптор кисти, используемый для закраски фона

        .. code-block:: cpp

            wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);


    .. cpp:member:: LPCTSTR lpszMenuName

        указатель на строку, содержащую имя меню

        .. code-block:: cpp

            wc.lpszMenuName = NULL;


    .. cpp:member:: LPCTSTR lpszClassName

        указатель на строку, содержащую имя класса окна

        .. code-block:: cpp

            wc.lpszClassName = szClassName;


    .. cpp:member:: HICON hIconSm

        дескриптор малой пиктграммы

        .. code-block:: cpp

            wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);


LoadIcon()
----------

.. cpp:function:: HUCON LoadIcon(HINSTANCE hInstance, LPCTSTR lpIconName)

    Загружает ресурс пиктограммы lpIconName из экземпляра приложения hInstance.

    Если hInstance NULL, то загружается системная иконка.

    * IDI_APPLICATION - пиктограмма приложения по умолчанию
    * IDI_ASTERISK, IDI_INFORMATION - информационная иконка
    * IDI_HAND, IDI_ERROR - иконка ошибка
    * IDI_EXCLAMATION, IDI_WARNING - иконка предупреждения
    * IDI_QUESTION - иконка вопроса
    * IDI_WINLOGO - логотип windows

    .. code-block:: cpp

        LoadIcon(NULL, IDI_APPLICATION)


LoadCursor()
------------

.. cpp:function:: HCURSOR LoadCursor(HINSTANCE hInstance, LPCTSTR lpCursorName)

    Загружает ресурс курсора lpCursorName из экземпляра приложения hInstance.

    Если hInstance NULL, то загружается системный курсор.

    * IDC_APPSTARTING - стрелка и малые песочные часы
    * IDC_ARROW - стрелка
    * IDC_CROSS - перекрестие
    * IDC_HELP - стрелка и вопросительный знак
    * IDC_IBEAM - текстовый двутавр
    * IDC_NO - перечеркнутый кружок
    * IDC_SIZEALL - четырехконечная стрелка
    * IDC_SIZENESW - двойная стрелка
    * IDC_SIZENS - двойная стрелка
    * IDC_SIZENWSE - двойная стрелка
    * IDC_SIZEWE - двойная стрелка
    * IDC_UPARROW - вертикальная стрелка
    * IDC_WAIT - песочные часы

    .. code-block:: cpp

        LoadCursor(NULL, IDC_ARROW);


CreateWindow()
--------------

.. cpp:function:: HWND CreateWindow(LPCTSTR lpClassName, LPCTSTR lpWindowName, DWORD dwStyle, int x, int y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lParam)

    * lpClassName - имя зарегистрированного окна

        Ранее регистрированное окно или из преопределенных

        * BUTTON
        * COMBOBOX
        * EDIT
        * LISTBOX
        * MDCLIENT
        * RICHEDIT
        * RICHEDIT_CLASS
        * SCROLLBAR
        * STATIC

    * lpWindowName - имя окна

    * dwStyle - стиль окна

        * WS_BORDER - окно с рамкой
        * WS_CAPTION - окно с заголовком
        * WS_CHILD - дочернее окно
        * WS_CLIPCHILDREN - исключить перерисовку дочерних окон
        * WS_CLIPSIBLINGS - исключить перерисовку соседних дочерних окон
        * WS_DLGFRAME
        * WS_GROUP - 
        * WS_HSCROLL - окно с горизонтальной прокруткой
        * WS_MAXIMIZE - развернутое окно
        * WS_MAXIMIZEBOX - окно с кнопкой разворачивания
        * WS_MINIMIZE - окно свернуто
        * WS_MINIMIZEBOX - окно с кнопкой сворачивания
        * WS_OVERLAPPED - перекрывающееся окно
        * WS_OVERLAPPEDWINDOW - WS_OVERLAPPED, WS_CAPTION, WS_SYSMENU, WS_THICKFRAME, WS_MINIMIZEBOX, WS_MAXIMIZEBOX
        * WS_POPUP - всплывающее окно
        * WS_POPUPWINDOW - WS_BORDER, WS_POPUP, WS_SYSMENU
        * WS_SYSMENU - окно с системным меню в области заголовка
        * WS_TABSTOP - 
        * WS_THICKFRAME - окно позволяет изменять его размеры
        * WS_VISIBLE - окно видимо
        * WS_VSCROLL - окно в сертикальной прокруткой

    * x - горизонтальная позиция, CW_USEDEFAULT
    * y - вертикальная позиция, CW_USEDEFAULT
    * nWidth - ширина окна, CW_USEDEFAULT
    * nHeight - высота окна, CW_USEDEFAULT
    * hWndParent - дескриптор родительского окна
    * hMenu - дескриптор меню окна или идентификатор жлемента управления
    * hInstance - дескриптор экземпляра приложения
    * lParam - указатель на данные, передаваемые в сообщении WM_CREATE


CreateWindowEx()
----------------

.. cpp:function:: HWND CreateWindowEx((DWORD dwExStyle, LPCTSTR lpClassName, LPCTSTR lpWindowName, DWORD dwStyle, int x, int y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lParam)

    * dwExStyle - расширенный стиль окна

        * WS_EX_ACCEPTFILES - окно принимает перетаскиваемые файлы
        * WS_EX_CLIENTEDGE - рамка имеет утопленный край
        * WS_EX_CONTROLPARENT - 
        * WS_EX_MDICHILD - 
        * WS_EX_STATICEDGE - 
        * WS_EX_TOOLWINDOW - 
        * WS_EX_TRANSPARENT - 
        * WS_EX_WINDOWEDGE - 


ShowWindow()
------------

.. cpp:function:: BOOL ShowWindow(HWND hWnd, int nCmdShow)



