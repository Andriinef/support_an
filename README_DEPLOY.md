# The deployment process is site DigitalOcean

Щоб розгорнути сервер на DigitalOcean, виконайте такі кроки:

1. Створіть обліковий запис DigitalOcean, якщо цього ще не зробили.
2. Після входу в свій обліковий запис DigitalOcean, натисніть кнопку "Create" (Створити) у верхній частині екрана і виберіть "Droplets" (Віртуальні машини).
3. Виберіть операційну систему, яку потрібно використовувати, і план сервера. У цьому кроці також можна налаштувати інші параметри, такі як кількість процесорів, обсяг оперативної пам'яті та місце на жорсткому диску.
4. Виберіть регіон сервера, в якому буде розгорнутий сервер.
5. Виберіть опцію "SSH Keys" (Ключі SSH) і додайте свій відкритий ключ SSH, щоб мати можливість підключатися до сервера через SSH без використання пароля.
Якщо у вас немає "SSH Keys" чи ви бажаєте створити новий, то (для Ubuntu):
    - Відкрийте термінал
    - Введіть команду

    ```code
    ssh-keygen -t rsa -b 4096 -C "hillel@gmail.com"
    ```

    де -C "hillel@gmail.com": додає коментар до ключа. Коментар допомагає ідентифікувати ключ і зазвичай визначається ім'ям користувача або адресою електронної пошти.
    - Коли ви побачите запит "Enter file in which to save the key" (Введіть ім'я файлу, до якого потрібно зберегти ключ) наприклад: hillel
6. Натисніть кнопку "Створити" внизу сторінки, щоб створити сервер.
7. Після створення сервера ви отримаєте інформацію про його IP-адресу та інші подробиці. Ви можете підключитися до сервера SSH, використовуючи свій локальний термінал і ключ SSH.

Це базовий процес розгортання сервера DigitalOcean. Далі ви можете встановити та налаштувати будь-яке ПЗ, яке вам необхідне для вашого проекту.

## Підключення до "Droplets" (Віртуальні машини) через термінал на локальному комп'ютері

Щоб підключитися до свого Droplet (віртуальної машини) на DigitalOcean через термінал, виконайте такі кроки:

1. Відкрийте термінал на локальному комп'ютері.
2. Використовуючи команду ssh, підключіться до Droplet, використовуючи IP-адресу або ім'я хоста сервера, а також ім'я користувача. Наприклад:

    ```code
    ssh root@46.93.137.131
    ```

3. Для спрощення підключення до сервера можливо сконфігурувати SSH config

    ```https
    https://www.ssh.com/academy/ssh/config
    ```

    наприклад:

    ```code
    # =========
    # [Hillel]
    # =========
    Host hillel
        HostName 46.93.137.131
        Port 22
        User root
        IdentityFily ~/.ssh/hillel
    ```

    Команда підключення до сервера:

    ```code
    .ssh hillel
    ```

## Встановлення та використання Docker та Docker-compose в Ubuntu 22.04

Дотримуйтесь цих кроків вказанних на сайті DigitalOcean:

```https
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04
```

## Клонування готового проекта до Droplet (віртуальної машини) з GitHab

Щоб клонувати готовий проект з GitHub до свого Droplet, Вам необхідно виконати наступні кроки:

1. Встановіть Git на Droplet, якщо він не встановлений. Для цього виконайте наступну команду в терміналі:

    ```code
    sudo apt-get update
    sudo apt-get install git
    ```

2. Створіть нову пару "SSH Keys" для GitHab командою:

    ```code
    ssh-keygen -t rsa -b 4096 -C "git@gmail.com"
    ```

    Програма ssh-keygen запуститься і попросить ввести шлях для збереження ключа. Залиште це поле порожнім, якщо ви хочете зберегти ключ у стандартному місці, а потім натисніть клавішу Enter.

3. За допомогою команди:

    ```code
    cat id_rsa.pub
    ```

    відкирийте файл id_rsa.pub з "SSH Keys" та зкопіюйте його.

4. Перейдіть до налаштувань GitHab та додайте "SSH Keys"

    ```markdown
    https://github.com/settings/keys
    ```

5. Клонуйте Git SSH командою:

    ```code
    git clone git@github.com:Andriinef/support_an.git
    ```

6. Команда:

    ```code
    ls -lа
    ```

    покаже всі клоновані та сховані файли з GitHub на вашій Droplet (віртуальної машини).

7. Копіюєм дані з файлу .env.default до .env файлу командою:

    ```code
    cp .env.default .env
    ```

8. У подальшому при зміні файлів на GitHub, зміни на Droplet (віртуальної машини) виконуються командою:

    ```code
    git pull
    ```

## Перший запуск проекту на  Droplet (віртуальної машини)

Щоб запустити проект на Droplet (віртуальної машини) за допомогою команд docker-compose виконайте наступні кроки:

1. Збираєм образи docker з вказаного файлу "docker-compose.yml" командою:

    ```code
    docker-compose build
    ```

2. Запустіть свій проект за допомогою команди:

    ```code
    docker-compose up -d
    ```

3. При потребі виконайте міграцію бази даних, використовуючи команду:

    ```code
    docker-compose exec app python src/manage.py migrate
    ```

4. Зареєструйте admin для проекту командою:

    ```code
    docsup='docker-compose exec app python src/manage.py createsuperuser'
    ```

5. Для збору статичних файлів у проекті використовують команду:

    ```code
    docker-compose exec app python src/manage.py collectstatic createsuperuser'
    ```

## Перевірка роботи проекта

Для перевірки роботи проекта на Droplet (віртуальної машини) виконайте наступні кроки:

1. Встановіть програму "Net-tools" якщо вона не була встановлена раніше. Цей набір утиліт для мережевого адміністрування в ОС Linux, який містить різні інструменти для налаштування та моніторингу мережі.

    ```code
    apt-get install net-tools
    ```

2. Введіть для відображення інформації про мережеві інтерфейси в системі, такі як IP-адреса, маска мережі, MAC-адреса тощо:

    ```code
    ifconfig
    ```

3. Ось приклад виконання команди ifconfig у терміналі Linux:

    ```yaml
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.10.5  netmask 255.255.255.0  broadcast 192.168.10.255
        inet6 fe80::20c:29ff:fe2f:8b08  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:2f:8b:08  txqueuelen 1000  (Ethernet)
        RX packets 19541  bytes 30743721 (29.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10212  bytes 1225488 (1.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1095  bytes 186284 (181.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1095  bytes 186284 (181.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ```

    В нашому випадку нам потрібен "eth0", у якому вказана потрібна нам адреса "192.168.10.5"

4. Відкрийте будь який браузер, наприклад "Google Chrome" та введіть отриманну адресу з додаванням порта ":8000" наприклад:

    ```http
    http://192.168.10.5:8000
    ```

    Ви побачите першу сторінку проекта.

### END
