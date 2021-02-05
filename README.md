# Python-Docker
A repository for exercice and workaround about docker

### How to build and launch
Build the image via the following commands :
```
$ docker build . -t docker_image
```

Run the container via this command :
```
$ docker run --name containertp -d -p 5000:5000 docker_image
```

### API
There are 4 routes for this application 
/ => home page
/books => display all books
/books/api/id/{id} => display book via the id
/books/api/title/{title} => display book with his title
