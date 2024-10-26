Чтобы создать виртуальное окружение в папке с проектом, выполните следующие шаги:

### 1. Откройте терминал или командную строку
Перейдите в папку с вашим проектом. Например:

```bash
cd /path/to/your/project
```

### 2. Создайте виртуальное окружение
Используйте команду `python -m venv`, чтобы создать виртуальное окружение. Вы можете назвать его как угодно, но обычно используют имя `venv`.

```bash
python -m venv venv
```

Эта команда создаст папку `venv` в вашем проекте, где будут храниться все файлы виртуального окружения.

### 3. Активируйте виртуальное окружение
Теперь вам нужно активировать виртуальное окружение. Команда активации зависит от операционной системы:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

После активации виртуального окружения, в командной строке появится префикс `(venv)`, указывающий на то, что вы работаете в виртуальном окружении.

### 4. Установите необходимые пакеты
Теперь вы можете устанавливать необходимые пакеты в виртуальное окружение, используя `pip`. Например:

```bash
pip install requests
```

### 5. Деактивируйте виртуальное окружение
Когда вы закончите работу, вы можете деактивировать виртуальное окружение, выполнив команду:

```bash
deactivate
```

Теперь вы вернетесь в глобальное окружение Python.

### 6. Добавьте `.gitignore` (опционально)
Если вы используете Git, рекомендуется добавить папку `venv` в `.gitignore`, чтобы она не попала в репозиторий. Создайте файл `.gitignore` в корне проекта и добавьте в него следующую строку:

```
venv/
```

Теперь ваше виртуальное окружение готово к использованию!




При создании виртуального окружения с помощью команды `python -m venv venv`, используется версия Python, которая связана с исполняемым файлом `python`, который вы вызываете. Если у вас установлено несколько версий Python, вы можете указать нужную версию, используя полный путь к исполняемому файлу Python.

### Примеры:

1. **Использование конкретной версии Python:**

   Если у вас установлена версия Python 3.9, и вы хотите создать виртуальное окружение с этой версией, вы можете использовать полный путь к исполняемому файлу Python 3.9:

   ```bash
   C:\Users\dergilev\AppData\Local\Programs\Python\Python311\python.exe
   C:\Python39\python.exe -m venv venv
   ```

2. **Использование версии Python, установленной через Anaconda:**

   Если у вас установлен Anaconda, и вы хотите использовать конкретную версию Python, установленную через Anaconda, вы можете использовать полный путь к исполняемому файлу Python из Anaconda:

   ```bash
   C:\Users\dergilev\Anaconda3\python.exe -m venv venv
   ```

3. **Использование версии Python, установленной через pyenv (на Linux/macOS):**

   Если вы используете `pyenv` для управления версиями Python, вы можете указать нужную версию следующим образом:

   ```bash
   pyenv exec python3.9 -m venv venv
   ```

### Пример:

Предположим, у вас установлена версия Python 3.9 в папке `C:\Python39`. Вы можете создать виртуальное окружение с этой версией следующим образом:

```bash
C:\Python39\python.exe -m venv venv
```

### Проверка версии Python в виртуальном окружении

После создания виртуального окружения, вы можете активировать его и проверить версию Python:

```bash
.\venv\Scripts\Activate.ps1
python --version
```

Это должно вывести версию Python, которую вы указали при создании виртуального окружения.

### Пример:

```bash
PS C:\Users\dergilev\Desktop\projects\OTUS-DEV\lesson.03> C:\Python39\python.exe -m venv venv
PS C:\Users\dergilev\Desktop\projects\OTUS-DEV\lesson.03> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\dergilev\Desktop\projects\OTUS-DEV\lesson.03> python --version
Python 3.11.0
(venv) PS C:\Users\dergilev\Desktop\projects\OTUS-DEV\lesson.03> pip install -r requirements.txt

```

Теперь вы знаете, как указать нужную версию Python при создании виртуального окружения.

Чтобы создать локальный репозиторий в директории `C:\Users\dergilev\Desktop\projects\OTUS-DEV` и связать его с удаленным репозиторием на GitHub, выполните следующие шаги:

### 1. Перейдите в директорию проекта

Откройте PowerShell и перейдите в директорию `C:\Users\dergilev\Desktop\projects\OTUS-DEV`:

```powershell
cd C:\Users\dergilev\Desktop\projects\OTUS-DEV
```

### 2. Инициализируйте Git репозиторий

Инициализируйте новый Git репозиторий в текущей директории:

```powershell
git init
```

### 3. Добавьте удаленный репозиторий

Свяжите ваш локальный репозиторий с удаленным репозиторием на GitHub:

```powershell
git remote add origin https://github.com/stormA4ka/OTUS-DEV.git
```

### 4. Добавьте файлы в индекс

Добавьте все файлы проекта в индекс Git:

```powershell
git add .
```

### 5. Сделайте первый коммит

Сделайте первый коммит с сообщением:

```powershell
git commit -m "Initial commit"
```

### 6. Создайте ветку `main` (если её нет)

Если ветка `main` не существует, создайте её:

```powershell
git checkout -b main
```

### 7. Отправьте изменения на удаленный репозиторий

Отправьте изменения на удаленный репозиторий:

```powershell
git push -u origin main
```

### Пример использования

Предположим, вы находитесь в директории `C:\Users\dergilev\Desktop\projects\OTUS-DEV`.

1. **Перейдите в директорию проекта**:
   ```powershell
   cd C:\Users\dergilev\Desktop\projects\OTUS-DEV
   ```

2. **Инициализируйте Git репозиторий**:
   ```powershell
   git init
   ```

3. **Добавьте удаленный репозиторий**:
   ```powershell
   git remote add origin https://github.com/stormA4ka/OTUS-DEV.git
   ```

4. **Добавьте файлы в индекс**:
   ```powershell
   git add .
   ```

5. **Сделайте первый коммит**:
   ```powershell
   git commit -m "Initial commit"
   ```

6. **Создайте ветку `main` (если её нет)**:
   ```powershell
   git checkout -b main
   ```

7. **Отправьте изменения на удаленный репозиторий**:
   ```powershell
   git push -u origin main
   ```
8. **Если ветка main уже существует, переключитесь на нее**:

   ```powershell
   PS C:\Users\dergilev\Desktop\projects\OTUS-DEV> git checkout -b main
   fatal: a branch named 'main' already exists  

   git checkout main
   ```


### Примечания

- Если ваш репозиторий использует ветку `master` вместо `main`, замените `main` на `master` в командах.
- Если вы уже добавили удаленный репозиторий, пропустите шаг 3.

Теперь ваш локальный проект должен быть успешно залит в удаленный репозиторий на GitHub.