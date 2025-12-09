# Учебный отчёт по Git, GitHub, SSH, GPG, PR, Rebase
## 1. Регистрация сервисов
- [✔] 1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется
- [✔] 2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации
- [✔] 3. Отправить зарегистрированный адрес почтового ящика личным сообщением
- [✔] 4. Отправить зарегистрированный логин личным сообщением
- [✔] 5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания

## 2. SSH
- [✔] 6. Сгенирировать **SSH** ключ и добавть его в список ключей для сервиса **GitHub**
```bash
ssh-keygen -t ed25519 -C "m.lissa5697@gmail.com"
```

![alt text](image.png)

Добавление на GitHub:
Через Settings -> SSH and GPG Keys

![alt text](image-1.png)
![alt text](image-2.png)

## 3. Personal Token
- [✔] 7. Сгенирировать **Personal Token** с правами **gist** и сохранить его в файл
Название: gist-token
Права: gist: read/write

![alt text](image-5.png)
![alt text](image-6.png)

## 4. GPG
- [✔] 8. Сгенерировать GnuGP для подтверждения подписания коммитов и возможно использование Х.509 (включить в отчет описание, что такое `smimesign`)
```bash
sudo apt install gnupg
gpg --full-generate-key
gpg --list-secret-keys --keyid-format=long
gpg --armor --export KEYID
```
![alt text](image-4.png)
![alt text](image-3.png)

Ключ добавлен в GitHub.

--armor - 

Описание smimesign:
S/MIME-подпись коммитов с X.509 сертификатами (корпоративный VPN/PKI).

## 5. Git config
- [✔] 9. Подготовить глобальные переменные окружения для **GitHub**
```bash
git config --global user.signingkey KEYID
git config --global commit.gpgsign true
git config --global tag.gpgSign true
git config --global user.name "Alice"
git config --global user.email "m.lissa5697@gmail.com"
git config --global core.editor "vim"
git config --global alias.co checkout
git config --global credential.helper "cache --timeout=3600"
git config --global core.autocrlf input
```


## 6. GitHub CLI
```bash
sudo apt install gh
gh auth login
```
✔ GitHub.com

✔ HTTPS

✔ token

✔ Yes → authorize

✔ Open browser

## 7. Создание папки
```bash
git init
gh repo create myproject --public --source=. --remote=origin
```
## 8. Создание папки
```bash
echo "# MyProject" > README.md
git add README.md
git commit -S -m "Initial commit: add README"
git push -u origin master
```

## 9. Создание папки
С «грязным» кодом:
```bash
print ("Hello appsec world" )
git add hello.py
git commit -S -m "Add dirty hello.py"
git push
```

## 9. Ветки, PR и rebase
```bash
git checkout -b patch1
git add hello.py
git commit -S -m "Add typer version"
git push -u origin patch1
gh pr create --base master --head patch1 --title "Patch1" --body "Typer implementation"
git add hello.py
git commit -S -m "Add code comments"
git push
```
patch1 → добавлен typer

patch2 + конфликты + rebase:
```bash
git checkout -b patch2
git add hello.py
git commit -S -m "Code style update"
git push -u origin patch2
```
patch2 → изменён стиль

PR:
```bash
gh pr create --base master --head patch2 --title "Patch2" --body "Style fixes"
```

получен конфликт → rebase → решён → PR merged

#какие права на репозитории существуют
#как в гитхаб можно заливать код, ssh http