# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from computer to the container
COPY . .

# Install the package (uses setup.py)
# This ensures all dependencies are installed and the package is recognized
RUN pip install .

# The command to run when the container starts
CMD ["play-blackjack"]