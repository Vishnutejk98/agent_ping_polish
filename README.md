# 🧠 agent_ping_polish

**agent_ping_polish** is a friendly AI agent built using the [Google Agent Developer Kit (ADK)](https://ai.google.dev/) that transforms boring, robotic notifications into cheerful, human-toned messages — designed to boost user engagement and make people smile.

---

## ✨ Features

- Rewrites dull system alerts into friendly, engaging messages
- Improves UX tone in apps with smile-worthy notifications
- Built using Google ADK with lightweight setup
- Runs quickly with [`uv`](https://github.com/astral-sh/uv) (or `pip`)

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone [https://github.com/Vishnutejk98/agent_ping_polish.git](https://github.com/Vishnutejk98/agent_ping_polish.git)
cd agent_ping_polish
```

### 2. Install dependencies

Using `uv` (recommended):

```bash
uv pip install -r requirements.txt
```

Or with `pip`:

```bash
pip install -r requirements.txt
```

### 3. Start the agent

```bash
uv run .
```

This will start the agent service and make it ready to receive notification messages for polishing.

---

## 📦 Example Usage

Send input:

```json
{ "input": "Battery low." }
```

Receive polished response:

```json
{ "output": "⚡ Battery’s feeling low — time for a quick recharge!" }
```

---


## 🛠 Built With

- 🧠 Google ADK
- ⚡ `uv` for environment management
- ❤️ Python 3.10+

---

## 📄 License

MIT License — feel free to use, modify, and share!

---

## 💬 Contact

Have feedback or questions? Reach out at [mailboxnumber04@gmail.com](mailto:mailboxnumber04@gmail.com).
