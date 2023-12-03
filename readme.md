# Face Tracker Server

This project is part of my Thesis Project, The Verge. It implements a Face Tracking function.

## Prerequisites

The project uses the following dependencies:

- Python 3.11.3
- Node.js 21.2.0

### Package Dependencies

- For `faceTracker` using python, see `requirements.txt`
   ** make requirements: `pip freeze > requirements.txt`
- For `server` using node.js, see `server/package.json`

## Setup

### 1. Python Virtual Environment

To set up the project, follow these steps:

1. Ensure that you have Python 3.11.3 installed on your machine.

2. Create a virtual environment:

```bash
python3.11.3 -m venv .venv
```

3. Activate the virtual environment. On Unix or MacOS, use:

```bash
source .venv/bin/activate
```

On Windows, use:

```
.venv\Scripts\activate
```

4. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Node.js

1. Ensure that you have Node.js 21.2.0 installed on your machine.
   (https://nodejs.org/download/release/v21.2.0/)

2. Install the required packages. On Unix or MacOS, use:

```bash
cd server
npm install
```

On Windows, use:

```bash
cd server
npm install
```





## Running the Project

### 1. Python Virtual Environment

1. Activate the virtual environment. On Unix or MacOS, use:

```bash
source .venv/bin/activate
```

On Windows, use:

```
.venv\Scripts\activate
```

2. Run the project:

```bash
python3.11.3 faceTracker.py
```



#### Windows PowerShell Execution Policy :

```
Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
```