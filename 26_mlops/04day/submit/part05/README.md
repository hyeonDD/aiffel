# image 빌드

```sh
docker build -t part05-api-server .
```

# container 실행

```sh
docker run -d --name api-server -p 8000:8000 part05-api-server
```

# swagger 화면

![swagger](images/swagger.png)
