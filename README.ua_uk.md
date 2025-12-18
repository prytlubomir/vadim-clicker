# Vadim's mouse

Додаток для автоматизаці миші, що контролюється призначенити клавішами клавіатури.

Створено за запитом Вадіма.

## Завантажити для Windows

Ви можете завантажити виконуваний файл з [офіційного вебсайту](https://prytlubomir.github.io/vadim-clicker-website/).

## Особливості

### Термінальна панель керування

Ви будь-коли можете переглянути чи змінити ваші гарячі клавіші.

<img alt="Terminal User Interface" src="https://prytlubomir.github.io/vadim-clicker-website/tui.png" width="700"/>

### Автоклікер

Натискає ліву кнопку миші, поки ви його не зупинете.

### Автотримач

Press and hold LBM untill released (either by manual click, or by automatic click)
Затискає ліву кнопку миші, поки ви не відпустите її вручну, або за допомогою `Автоклікера`.

## Зібрати з вихідного коду

### 1. Клонуйте репозиторій
`git clone https://github.com/prytlubomir/vadim-clicker`
### 2. Перейдіть у директорію
`cd vadim-clicker`
### 3. Налаштуйте віртуальне оточення
`uv sync`
### Зберіть для Windows
`uv run build.py`

В результаті має вийти виконуваний файл `main.exe`