# Как запустить проект

## Установка проекта
<pre><code>git clone https://github.com/Ulukbek2424/interview_project.git</code></pre>

## Запуск проекта (запускать с директории, где лежит докерфайл)
<pre><code>docker build -t mydjangoapp .</code></pre>
<pre><code>docker run -d -p 8081:8081 --name mydjangoapp-container mydjangoapp</code></pre>
**Я поднимал на 8081 порту, т.к остальные на моей машине были заняты, вы можете поднимать на тех портах, на которых вам удобно)**

## Тестирование и просмотр 
- добавление новых записей осуществляется в админ панели (url - /admin)
- тестировать API можно в swagger (url - /docs)

## Что можно было еще добавить
- docker volumes для хранения данных с БД на локальной машине (если вдруг что произойдет с контейнером)
- отдельный контейнер для БД, и прооркестрировать все в docker-compose
- в отдельный файл или сервис вынести все ключи и токены приложения