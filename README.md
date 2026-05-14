# JSE Network — Ownership Visualizer

An interactive network visualization that maps board-of-director connections across companies listed on the Jamaica Stock Exchange. Built with Flask, SQLite, and vis.js, powered by live data from the [Stacks JSE API](https://stacksja.com/developers).

## Why This Exists

Jamaica's stock market is tightly interconnected — the same directors often sit on multiple boards, creating a web of influence that isn't visible from a standard stock screener. This tool makes those connections visible at a glance.


## Features

- **Live JSE data** — fetches all listed companies and their boards of directors from the Stacks API
- **Network graph** — companies rendered as interactive nodes, with shared directors shown as connections
- **Company details** — click any node to see its market, price, full board of directors, and board connections
- **Director role badges** — chairman, executive, non-executive, and independent roles are color-coded
- **Connection tracing** — click a connection card to navigate directly to the linked company
- **Main vs Junior Market** — nodes are color-coded green (Main Market) and blue (Junior Market)

## Tech Stack

- **Python / Flask** — backend API and routing
- **SQLite** — local data storage for companies and directors
- **vis.js** — network graph rendering and physics simulation
- **Stacks JSE API** — live market data, director information, and company details
- **HTML / CSS / JavaScript** — frontend interface

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/jse-network.git
cd jse-network

# Install dependencies
pip install -r requirements.txt

# Add your Stacks API key
echo "STACKS_API_KEY=pk_your_key_here" > .env
```

Get a free API key at [stacksja.com/developers](https://stacksja.com/developers).

## Usage

```bash
# Start the server
python run.py
```

Open `http://127.0.0.1:5000` in your browser and click **Load JSE data**.

## Project Structure

```
jse-network/
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── routes.py         # API routes and page serving
│   ├── data.py           # Stacks API integration and data loading
│   ├── db.py             # SQLite database layer
│   └── templates/
│       └── index.html    # Frontend with vis.js network graph
├── .env                  # API key (not committed)
├── .gitignore
├── README.md
├── requirements.txt
└── run.py                # Entry point
```

## How It Works

1. **Fetch** — pulls all listed companies and their boards of directors from the Stacks JSE API
2. **Store** — saves company and director data to a local SQLite database
3. **Process** — runs a self-join query on the directors table to find individuals who sit on multiple boards
4. **Visualize** — serves the processed data as JSON to a vis.js network graph on the frontend

## What I Learned

- Building a full-stack web application with Flask
- Integrating with a third-party REST API (Stacks JSE)
- Relational database design with SQLite (self-joins for network detection)
- Frontend data visualization with vis.js
- Structuring a Python project with separation of concerns (routes, data, database)
- Working with environment variables to manage API keys securely