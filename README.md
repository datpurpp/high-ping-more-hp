# Dynamic Lag Balancer (High Ping? Get More HP!) 🎮

An open-source Python utility designed for multiplayer video games that balances the playing field for players connecting from across the world. If a player experiences high network latency (ping), the script dynamically calculates and awards them additional Health Points (HP) to compensate for their lag.

## 🚀 Features
* **Real-time Scaling:** Dynamically maps network latency directly to player health metrics.
* **Open Canvas Architecture:** Built cleanly in Python to serve as an upgradable base style project.
* **Customizable Progression:** Easily tweak thresholds to fit the natural rules and physics of your specific game.

## 📊 Ping-to-HP Scaling Chart
The program uses a structured scaling system to balance high latency:

| Ping (Milliseconds) | Player Health (HP) | Status |
| ------------------- | ------------------ | ------ |
| 20 ms               | 100 HP             | Normal |
| 60 ms               | 105 HP             | Scaled |
| 500 ms              | 225 HP             | Max Balance |

*Note: Ping values between 500ms and 750ms maintain the maximum balanced cap of 225 HP.*

## 💻 Getting Started

### Prerequisites
Make sure you have Python installed on your machine.

### Installation
1. download & run antilag.py

 download

 open powershell on windows

   ```
3. Navigate to the project folder:
   cd foldername
   ```

### Running the Program
Execute the main script using the following command:
python antilag.py
```

## 🛠️ Contributing & Upgrades
This project is open-source and meant to be upgraded and developed further! Feel free to fork the repository, optimize the networking code, integrate it with existing game engines, or add custom physics rules. 

If you make an upgrade, submit a **Pull Request** so we can build the ultimate multiplayer lag balancer together!
