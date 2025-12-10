# 🃏 Blackjack Game (Dockerized)

Welcome to the **Blackjack Game**!  
This project packages a simple interactive Blackjack console game inside a Docker container so you can run it anywhere with zero setup beyond Docker.

---

## 📦 1. Build the Docker Image

Before running the game, build its Docker image.  
Run this inside the project folder (where your Dockerfile is located):


docker build -t blackjack-game .

## Run the Game

Because Blackjack is an interactive console game, you must use -it so you can type into the container.

docker run -it blackjack-game
