docker build --no-cache -t dineshsonachalam/adp:latest .
echo "Build is completed!"
docker push dineshsonachalam/adp:latest
echo "Docker push is completed!"
#docker run -p 8087:8087 dineshsonachalam/adp:2.0.0


