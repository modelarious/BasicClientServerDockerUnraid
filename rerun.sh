

docker build -t docker-server-unraid .

docker rm flask-echo-server
docker run --rm -p 5000:5000 --name flask-echo-server docker-server-unraid:latest


