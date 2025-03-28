# 🧱 Breakout Game (90s Style)

A retro-style Breakout game built using Python and the Turtle graphics library.
![image](https://github.com/user-attachments/assets/9e5d29ee-1ff8-4204-8783-c6bbfcf9af47)

## 🎮 Gameplay

Control the paddle to bounce the ball and break the colored bricks at the top. If the ball falls below the paddle, it resets. Score points by destroying bricks!

## 🛠 Features

- Paddle movement (Left and Right arrows)
- Ball with realistic bounce mechanics
- Brick wall with 3 color tiers
- Scoring system
- Game reset after ball is missed
- Collision cooldown to prevent multiple bounces on paddle

## 🧩 Project Structure

```
.
├── main.py         # Main game loop and logic
├── ball.py         # Ball behavior and movement
├── paddle.py       # Paddle controls and behavior
├── bricks.py       # Brick creation
├── scoreboard.py   # Score tracking
└── README.md       # Project info
```

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed.
2. No external libraries needed — only uses the built-in `turtle` and `time` modules.
3. Run the game:

```bash
python main.py
```

Use the **Left** and **Right** arrow keys to move the paddle.

## ✅ Fixes & Notes

- Added a cooldown (`paddle_hit_ready`) to avoid multiple paddle bounces in a single frame.
- Bricks are recreated after a ball miss.
- All elements reset properly after life loss.




---

Have fun breaking bricks! 🕹️


