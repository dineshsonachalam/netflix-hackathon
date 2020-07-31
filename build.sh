docker build --no-cache -t dineshsonachalam/adp:2.0.0 .
echo "Build is completed!"
docker push dineshsonachalam/adp:2.0.0
echo "Docker push is completed!"
#docker run -p 8087:8087 dineshsonachalam/adp:2.0.0


