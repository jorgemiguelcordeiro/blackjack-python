# 🃏 Blackjack Game (Dockerized)

Welcome to the **Blackjack Game**!  
This project packages a simple interactive Blackjack console game inside a Docker container. It demonstrates Object-Oriented Programming (OOP) principles in Python and modern deployment using Docker, allowing you to run the game anywhere with zero setup.

---

## 🚀 How to Run

### 1. Build the Docker Image
Run this command in your terminal inside the project root folder (where the `Dockerfile` is located).

**Windows (PowerShell/CMD):**

```bash
docker build -t blackjack-game .
```
### 2. Start the Game

```bash
docker run -it blackjack-game 
```

---

## Future work & Improvements

While this project currently handles a single round of gameplay, here is how the architecture is designed to scale.

### 1\. Adding Multiple Rounds (Game Loop)

Currently, the game plays one hand and exits. To allow continuous play:

*   **The Logic:** We would wrap the game flow in game.py inside a while True loop.
    
*   This requires adding a \`reset\_round()\` method to clear the \`self.player.hand\` lists and potentially re-shuffle if the deck is running low.
    

### 2\. From Version Control to Full CI/CD

Currently, this project uses **Version Control** (Git) and **Deployment** packaging (Docker). The next step is to implement a full **CI/CD Pipeline**.

*   **Continuous Integration (CI):**  _Goal:_ Ensure code doesn't break when new features are added.
    
    *   _How:_ Use **GitHub Actions** to automatically install the package and run unit tests (pytest) every time code is pushed to the repository.
        
*   **Continuous Deployment (CD):**
    
    *   _Goal:_ Automate the release of the software.
        
    *   _How:_ Configure GitHub Actions to automatically build the Docker image and push it to **Docker Hub** whenever the CI tests pass. This allows users to download the latest version simply by running docker pull.
        

🧠 Design Discussion & "What If" Questions
------------------------------------------

Here are potential questions that explore the design choices.

### Q1: Why use pop() to deal cards?

**Answer:** We deal from the end of the list using .pop() because it is an **O(1)** operation (Constant Time). Removing the _first_ card (pop(0)) would force Python to shift every remaining item in the list one spot to the left, which is an **O(N)** operation (Linear Time) and computationally less efficient.

### Q2: How would we handle "Aces" being 1 or 11?

**Answer:** Currently, we simplified Aces to 11. To implement the real rule:

*   We would modify the @property def total(self) in player.py.
    
*   **Logic:** Calculate the sum assuming Aces are 11. If the total is > 21 and we have an Ace, subtract 10 from the total (effectively turning an 11 into a 1) until the total is <= 21 or we run out of Aces.
    

### Q3: Why is Deck created inside BlackjackGame instead of passed in?

**Answer:** This is a choice between **Composition** and **Dependency Injection**.

*   _Current (Composition):_ The Game "owns" the Deck. This is simple and self-contained.
    
*   _Alternative (Dependency Injection):_ Passing the deck in (\_\_init\_\_(self, deck)) would be better for testing, allowing us to pass a "rigged" deck to test specific scenarios (like forcing a Bust).
    

### Q4: How would we add Betting?

**Answer:**

1.  Add a self.balance attribute to the Player class.
    
2.  Update play\_round to ask for a wager amount before dealing.
    
3.  If the player wins, self.balance += wager; if they lose, self.balance -= wager.
    
4.  This would require persistence (saving the balance) if we want it to last across different program runs (e.g., using a SQLite database or a JSON file).