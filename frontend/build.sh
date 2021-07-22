#!/bin/bash
npm run build
docker build -t dineshsonachalam/netflix-hackathon-frontend:latest .
docker push dineshsonachalam/netflix-hackathon-frontend:latest