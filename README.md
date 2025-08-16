# Order Execution Engine

## 📌 Overview

A lightweight order execution engine that simulates token swaps across two Solana-based DEXs — **Raydium** and **Meteora** — allowing you to test swap logic and evaluate execution quality before wiring real capital. Trades are routed based on mocked liquidity, price impact and timing to imitate realistic swap behaviour.

## ⚙️ Tech Stack Used

* **Python 3.11** — high‑level, fast to prototype execution logic while remaining production ready

* **FastAPI** — modern async framework to expose REST/WebSocket endpoints with minimal overhead

* **Redis** — lightweight in‑memory datastore used for pub‑sub messaging and fast job queuing between workers

* **HTML/JS (static folder)** — frontend layer used only for local testing and manual triggering

* **WebSockets** — to push real‑time orderbook updates / execution status to UI

* **Pydantic & SQLite** — easy‑to‑manage model validation + persistence layer

* **Python 3.11** — core engine logic

* **FastAPI** — REST endpoints

* **HTML/JS** — minimal front‑end interface

* **WebSockets** — mock orderbook + real‑time updates

* **Pydantic & SQLite** — models and storage

## 🚀 Setup & How to Run

```bash
# Start Redis (required for job queue / pub-sub)
redis-server &

# (Optional) Make SQLite DB accessible — create file & run migrations
touch engine.db
# Or change DB path in db.py to a full path if using external DB

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
python app.py
```

Static files (like `index.html`) reside under the `static/` directory — the UI can be accessed by navigating to `http://localhost:8000` after starting the server.

### 📊 Accessing the Database

By default, the engine uses `SQLite` and stores data in `engine.db`. You can inspect/debug the database at any time using any SQLite client:

```bash
sqlite3 engine.db
sqlite> .tables   # view tables
sqlite> SELECT * FROM orders;  # inspect data
```

To connect from GUI clients (e.g. **DB Browser for SQLite**, **TablePlus**), simply point them to the `engine.db` file in the root directory. If using a remote path or Docker, ensure the file is mounted or the path in `db.py` is updated accordingly.

```bash
# Start Redis (required for job queue / pub-sub)
redis-server &

# (Optional) Make SQLite DB accessible — create file & run migrations
touch engine.db
# Or change DB path in db.py to a full path if using external DB

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
python app.py
```

Static files (like `index.html`) reside under the `static/` directory — the UI can be accessed by navigating to `http://localhost:8000` after starting the server. Ensure the database file path in `db.py` is reachable (e.g. use an absolute path if running inside Docker or different directory).

```bash
# Start Redis (required for job queue / pub-sub)
redis-server &

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
python app.py
```

Static files (like `index.html`) reside under the `static/` directory — the UI can be accessed by navigating to `http://localhost:8000` after starting the server.

```bash
# 1. Clone the repo and cd into it
pip install -r requirements.txt

# 2. Run the FastAPI backend
python app.py

# 3. Open the UI (index.html) in your browser
```

The engine will begin simulating swaps between Raydium & Meteora using your order instructions. Logs will show execution path and mocked fill details.

## 📄 Why Market Orders?

Market orders guarantee **speed of execution**, which is crucial in volatile crypto markets. They serve as a strong baseline and provide stress‑testing capabilities for the engine.

### 🔮 Extending to Other Order Types

* **Limit Orders**: add price thresholds before swap execution
* **Sniper Orders**: trigger execution once a highly specific on‑chain/tick criterion is met

> Both are extensions of the same execution engine — simply add pre‑trade validation conditions before routing to swap.

## 🔭 Future Scope

* Integrate with *real* DEX SDKs (e.g. Raydium SDK, Phoenix, Jupiter) for live market routing
* Plug into **trading view / strategy layer** for automated signal‑based execution
* Add L2 **order‑driven backtesting** framework
* Support multi‑hop and cross‑DEX routing for best price fills

## 📁 Project Structure

```text.
.
├── app.py               # FastAPI app & routing
├── workers.py           # background simulated executors
├── websocket_manager.py # mock orderbook/ws messaging
├── models.py            # DB + order models
├── utils.py             # helper functions
├── db.py                # DB connection
├── index.html           # frontend (local test)
└── requirements.txt
```

## 🧑‍💻 Contributing

1. Fork
2. Add features in new branch
3. Raise PR 🔁

## 📬 License

MIT — use freely. Open to collaborations!
