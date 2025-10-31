
## 🪨✋✂ Rock Paper Scissors Game 🎮

### *A simple yet fun Python terminal game built by [Adil Tofiq Mulla](https://github.com/AdilTofiqMulla)*

---

### 🧠 **About the Project**

This is a Python-based implementation of the classic **Rock, Paper, Scissors** game — with a login system, life counter, score tracker, and rule display.
It runs entirely in the terminal and offers a nostalgic gaming experience while improving Python logic and condition handling skills.

---

### ⚙️ **Features**

✅ Username and Password login system (reads from `accounts.txt`)
✅ Dynamic score, lives, and draw tracking
✅ “Rules” and “Display Lives/Score/Draws” commands during gameplay
✅ Randomized computer choices using the `random` module
✅ ASCII-styled intro with emojis 🤘 ✋ ✂
✅ Simple game logic and flow with clear win/lose conditions

---

### 💥 **Problems Faced & How They Were Solved**

#### 1️⃣ **Rule Command Not Showing**

**Problem:** Typing `rules` or `display lives` wasn’t printing anything.
**Cause:** All checks used separate `if` statements without `elif`, so logic skipped parts or got overridden by earlier conditions.
**Solution:** Rewrote logic using `if/elif/else` structure to ensure only one branch runs per input.

---

#### 2️⃣ **Lives/Score Updates Not Working Properly**

**Problem:** Score or lives didn’t change as expected for some moves.
**Cause:** Wrong conditions and inconsistent increment/decrement logic.
**Solution:** Cleaned and standardized the win/loss/draw handling for each move.

---

#### 3️⃣ **Git Index Lock Error**

**Problem:**

```
fatal: Unable to create '.git/index.lock': File exists
```

**Cause:** A previous Git process didn’t finish, leaving a lock file.
**Solution:** Removed the file manually using:

```bash
rm -f .git/index.lock
```

and ensured no Git process was running in the background.

---

#### 4️⃣ **Username/Password Validation Not Working**

**Problem:** Access was granted even for invalid users.
**Cause:** Incorrect condition: `if username and password in password_list:`
**Solution:** Fixed with:

```python
if username in password_list and password in password_list:
```

(or a proper mapping for secure validation).

---

### 🧩 **How to Run the Game**

#### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/<your-username>/RPSgame.git
cd RPSgame
```

#### **2️⃣ Add Your Accounts File**

Create a file named `accounts.txt` in the same directory:

```
username1
password1
username2
password2
```
or  run the RPS_account_setup file using given below command and it will store the info in a new file
```bash
python RPS_account_setup.py
```
<img width="601" height="242" alt="image" src="https://github.com/user-attachments/assets/f1d3e9c1-2d74-4f17-9eba-4075d3904251" />


#### **3️⃣ Run the Game**

```bash
python main.py
```
<img width="1039" height="814" alt="image" src="https://github.com/user-attachments/assets/3f62c6fe-0bfa-44fc-86dc-29be1ade95e1" />

---

### 🕹️ **Gameplay Commands**

| Command                      | Description               |
| ---------------------------- | ------------------------- |
| `rock` / `paper` / `scissor` | Play your move            |
| `rules`                      | Display game rules        |
| `display lives`              | Show your remaining lives |
| `display score`              | Show your score           |
| `display draws`              | Show total draws          |
| `exit`                       | Quit the game             |

---

### 🧑‍💻 **Tech Stack**

* **Language:** Python
* **Libraries:** `random`, `time`
* **IDE:** Visual Studio Code

---

### ✨ **Future Improvements**

* Add color-coded output using `colorama`
* Use JSON for secure login system
* Add multiplayer or GUI version using `tkinter` or `pygame`

---

### 🏁 **Credits**

Created with ❤️ by **Adil Tofiq Mulla**

> “Rock hard, code harder 🤘”

---
