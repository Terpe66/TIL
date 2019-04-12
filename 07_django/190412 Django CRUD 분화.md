`GET /Articles/1`

- `id`가 1인 Article의 페이지로 이동

`GET /Articles/`

- Article의 목록 페이지로 이동

`POST /Articles/`

- Article의 목록을 수정



Create - POST

Read - GET

Update - PUT / PATCH * 우리는 PATCH를 배움

- PUT : 전체를 지우고 다시 만듦
- PATCH : 수정할 부분만 지우고 다시 만듦

Delete - DELETE



`POST /Articles/`

- 새로운 Article을 만드는 요청

`PATCH /Articles/1`

- Articles에서 `id`가 1인 Article을 수정하는 요청

`GET /Articles/1`

- Articles에서 `id`가 1인 Article을 받아오는 요청

`DELETE /Articles/1`

- Articles에서 `id`가 1인 Article을 삭제하는 요청

`POST /Articles/1`

- 틀림 : 새로운 Article을 만드는 요청에 `id`가 붙을 수 없다



**`GET /articles/1/` : 1번 조회**

`GET /articles/` : 전체 조회



**`GET /articles/1/edit/` : 1번 수정하는 페이지**

`PATCH /articles/1/` : 1번 수정



**`GET /articles/new/` : 1번 생성하는 페이지**

**`POST /articles/` : 새로 생성**



`DELETE /article/1/` : 1번 삭제