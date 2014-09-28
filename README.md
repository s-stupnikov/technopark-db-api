technopark-db-api
=================

Суть задания заключается в реализации API к базе данных проекта «Форумы» по документации к, собственно, этому API, т.е. эдакий реверс-инжиниринг.
Таким образом, на входе:
* документация к API
на выходе:
* поднятый и настроенный MySQL
* БД где будет хранится информация об основных сущностях системы
* вэб-сервер, который будет отвечать на внешние запросы, обращаясь к БД

После написания API правильность реализации будет проверяться с помощью автоматического функционального тестирования.
Методика тестирования:
* запускается скрипт на python, который будет проводить тестирование
* он опрашивает все методы, определенные в API, по шаблону http://{{student_ip}}/db/api//{{entity}}/{{method}}/ с заранее заданными\случайными параметрами, корректными относительно документации (в POST-запросах передается json, GET - как обычно)
* ответы вашей системы сравниваются с эталонами
* если код http ответа не 200, то тест считается проваленным
* если в ответе не хватает каких-то полей или значение каких-то полей не совпадает, то тест считается проваленным
* если нет ни одного неправильного ответа, то тест считается пройденным
* результат тест отправляется вам на почту

##FAQ
1. Что нужно ответить, если создаваемый объект\связь уже существует?
  - Нужно ответить этим уже созданным объектом для всех сущностей, кроме юзера. В случае юзера вернуть ошибку (см. п. 4 и 2)

2. Что такое code в ответах на запросы?
  - Код возврата: 
    * 0 — ОК, 
    * 1 — запрашиваемый объект не найден,
    * 2 — невалидный запрос (например, не парсится json),
    * 3 — некорректный запрос (семантически),
    * 4 — неизвестная ошибка.
    * 5 — такой юзер уже существует

3. Юзер может несколько раз голосовать за один и тот же пост или тред?
  - Да
4. Что отвечать в случае ошибки?
  - {"code": *code*, "response": *error message*}
5. Что делать при удалении треда\поста? 
  - Сущность помечается, как isDeleted. Для поста помечается только он сам, для треда - все его внутренности. При этом удаленные сущности не учитываются при подсчете, например, количества постов в треде, но передаются в теле ответа.
6. Уникален ли username?
  - Нет, уникален email
7. Уникален ли name у Forum?
  - да, как и shortname
8. Что такое related user у Forums.details?
  - Показать полную информацию о создателе форума (вместо просто его email-а)
9. Что за типы сортировок для постов ['flat', 'tree', 'parent_tree']?
  - Есть три вида сортировок с пагинацией, они оказываются очень интересными:
    * по дате (flat), комментарии выводятся простым списком по дате,
    * древовидный (tree), комментарии выводятся отсортированные в дереве по N штук,
    * древовидные с пагинацией по родительским (parent_tree), на странице 25 родительских комментов и все комментарии прикрепленные к ним, в древвидном отображение,

  У всех вариантов есть asc и desc сортировки.

#API Documentation

##Общие
* [clear](./doc/clear.md)

##Forum
* [create](./doc/forum/create.md)
* [details](./doc/forum/details.md)
* [listPosts](./doc/forum/listPosts.md)
* [listThreads](./doc/forum/listThreads.md)
* [listUsers](./doc/forum/listUsers.md)

##Post
* [create](./doc/post/create.md)
* [details](./doc/post/details.md)
* [list](./doc/post/list.md)
* [remove](./doc/post/remove.md)
* [restore](./doc/post/restore.md)
* [update](./doc/post/update.md)
* [vote](./doc/post/vote.md)

##User
* [create](./doc/user/create.md)
* [details](./doc/user/details.md)
* [follow](./doc/user/follow.md)
* [listFollowers](./doc/user/listFollowers.md)
* [listFollowing](./doc/user/listFollowing.md)
* [listPosts](./doc/user/listPosts.md)
* [unfollow](./doc/user/unfollow.md)
* [updateProfile](./doc/user/updateProfile.md)

##Thread
* [close](./doc/thread/close.md)
* [create](./doc/thread/create.md)
* [details](./doc/thread/details.md)
* [list](./doc/thread/list.md)
* [listPosts](./doc/thread/listPosts.md)
* [open](./doc/thread/open.md)
* [remove](./doc/thread/remove.md)
* [restore](./doc/thread/restore.md)
* [subscribe](./doc/thread/subscribe.md)
* [unsubscribe](./doc/thread/unsubscribe.md)
* [update](./doc/thread/update.md)
* [vote](./doc/thread/vote.md)

