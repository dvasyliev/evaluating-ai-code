About me ◽️ 🎬 Udemy Instructor ◽️ 👨🏻‍💻 Front-End Engineer (10+ years) ◽️ 🎯 Mentor for Developers

# Evaluating AI Code

This repository contains the Source Code for the 🧑🏻‍💻 [AI Code Review: Evaluate Python Code with Confidence](https://go.dvasyliev.com/evaluating-ai-code) course.

A small command-line calculator in Python, used as the subject of an AI code-review exercise. The repository contains both the application and the AI configuration (`CLAUDE.md`, rules and skills) that guide how an AI assistant works on it.

# My Other Courses

#### Agentic AI Courses

🦞 [OpenClaw for Developers: AI Coding Crash Course](https://go.dvasyliev.com/openclaw)

#### AI Tools Courses

🔍 [AI Code Review: Evaluate Python Code with Confidence](https://go.dvasyliev.com/evaluating-ai-code)\
🧑🏻‍💻 [Claude Code: AI Crash Course for Developers](https://go.dvasyliev.com/claude-code)\
😈 [GitHub Copilot for Beginners: AI Coding Crash Course](https://go.dvasyliev.com/copilot)\
👻 [Cursor AI for Beginners: AI Coding Crash Course](https://go.dvasyliev.com/cursor)\
🏄🏻‍♂️ [Windsurf for Beginners: AI Coding Crash Course](https://go.dvasyliev.com/windsurf)\
🪐 [Google Antigravity for Beginners: AI Coding Crash Course](https://go.dvasyliev.com/antigravity)

#### AI Certifications Courses

🏅 [CCA-F: Claude Certified Architect — Complete Exam Preparation](https://go.dvasyliev.com/cca-f)\
📜 [GH-300: GitHub Copilot Exam Preparation](https://go.dvasyliev.com/gh300)\
📝 [GH-300: GitHub Copilot Practice Certification Exam](https://go.dvasyliev.com/gh300-practice)

#### Vibe Coding Courses

⚡ [Vibe Coding for Developers: v0, AI, Supabase, Vercel Deploy](https://go.dvasyliev.com/v0)\
❤️ [Lovable AI: Complete Guide for Vibe Coding](https://go.dvasyliev.com/lovable)

#### Front-End Courses

⚛️ [React Crash Course: From Zero to Hero](https://go.dvasyliev.com/react)\
🤖 [React.js AI Chatbot App with ChatGPT and Gemini AI](https://go.dvasyliev.com/ai-chatbot)

#### Full-Stack Courses

👓 [Next.js Crash Course: Build a Full-Stack App in a Weekend](https://go.dvasyliev.com/nextjs)\
🧩 [Node.js Crash Course: Build a REST API in a Weekend](https://go.dvasyliev.com/nodejs)

#### Other Courses

👣 [AI Agents with OpenAI AgentKit: Hands-On Guide](https://go.dvasyliev.com/agentkit)\
💬 [ChatGPT for Developers: AI Coding Crash Course](https://go.dvasyliev.com/chatgpt)

# How to use Code Examples from Github

## Download the code source

### a) Download code source for final application

1. Open repository main [page](https://github.com/dvasyliev/evaluating-ai-code).

2. Click on the green "Code" button to open a list and then click on the "Download ZIP" button to download a source code.

<img width="472" alt="Screenshot 2024-06-25 at 17 34 44" src="https://github.com/dvasyliev/react-crash-course/assets/24624324/5e67c693-39fd-4262-b0ff-7aa81f439642">

### b) Download code sources for specific lesson

1. Open [commits](https://github.com/dvasyliev/evaluating-ai-code/commits/main/) page.

2. Click on the "code" icon near the lesson you are interested.

<img width="1319" alt="Screenshot 2024-06-25 at 17 48 06" src="https://github.com/dvasyliev/react-crash-course/assets/24624324/53caf0fe-7d61-4c22-b10f-33b8f1cb5512">

3. You will be redirected to the specific source code page for this lesson.

4. Click on the green "Code" button to open a list and then click on the "Download ZIP" button to download a source code.

<img width="472" alt="Screenshot 2024-06-25 at 17 34 44" src="https://github.com/dvasyliev/react-crash-course/assets/24624324/5e67c693-39fd-4262-b0ff-7aa81f439642">

## Open project in the VS code (code editor)

Open the archive on your computer, open VS code (code editor) and cick "File" -> "Open Folder" -> Choose project folder => "Open".

<img width="470" alt="Screenshot 2024-06-25 at 17 40 31" src="https://github.com/dvasyliev/react-crash-course/assets/24624324/ec7661e5-d8e7-409f-a935-5a55335553e9">

# About the Project

Everything runs on the Python standard library. There are no dependencies to install.

## The application

`calculator.py` is an interactive menu loop. You pick an operation, enter one or two numbers, and it prints the result rounded to two decimals. The last five results are kept in a bounded history.

Menu keys: `1`–`7` for the operations, `h` for history, `q` to quit.

### Operations

| Key | Operation                  | Input          | Rejected input                                                                     |
| --- | -------------------------- | -------------- | ---------------------------------------------------------------------------------- |
| `1` | Add                        | two numbers    | —                                                                                  |
| `2` | Subtract                   | two numbers    | —                                                                                  |
| `3` | Multiply                   | two numbers    | —                                                                                  |
| `4` | Divide                     | two numbers    | a divisor of zero                                                                  |
| `5` | Power                      | base, exponent | zero base with a negative exponent; an exponent above 100; a result that overflows |
| `6` | Square root                | one number     | a negative number                                                                  |
| `7` | Percentage                 | value, percent | a negative percent                                                                 |
| `h` | Show the last five results | —              | —                                                                                  |
| `q` | Quit                       | —              | —                                                                                  |

Rejected input prints an error and returns to the menu; nothing is added to the history. An empty entry at a number prompt is rejected the same way.

## AI configuration

Three files steer an AI assistant working in this repository.

| File                                     | Loaded                  | What it does                                                                                                                                                         |
| ---------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CLAUDE.md`                              | always                  | Behavioural guidelines: state assumptions before coding, keep it simple, make surgical changes, define success criteria and verify.                                  |
| `.claude/rules/python.md`                | when touching `**/*.py` | Python rules with a bad and a good example each — raise instead of print, name constants, bound anything that grows, catch specific exceptions, and so on.           |
| `.claude/skills/ai-code-review/SKILL.md` | on request              | A review pass over AI-generated code: correctness, error handling, tests, quality and performance, security. Reports findings by severity and ends with a checklist. |

`calculator.py` is written to follow the Python rules, which is why it raises `ValueError` instead of printing, uses named constants, and keeps history in a bounded `deque`.

## Installing Python

The project needs Python 3.6 or newer. Check what you have:

```bash
# Mac/Linux
python3 --version

# Windows
python --version
```

If that fails, install it. macOS ships no usable Python by default — `python3` is a stub that offers to install the Command Line Tools. Most Linux distributions already include it. On Windows, tick **Add Python to PATH** in the python.org installer.

```bash
# Mac
xcode-select --install       # Apple's Command Line Tools
brew install python          # or Homebrew, for a newer version

# Linux
sudo apt install python3     # Debian, Ubuntu
sudo dnf install python3     # Fedora

# Windows
Download python from https://www.python.org/downloads/ or the Microsoft Store
```

## Running the app

```bash
# Mac/Linux
python3 calculator.py

# Windows
python calculator.py
```

Example session:

```
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square root
7. Percentage
h. History   q. Quit
Choose: 1
First number: 2
Second number: 3
Result: 5.0
```

## Running the tests

The suite is `test_calculator.py`, written with the standard-library `unittest` module. Fourteen tests cover the arithmetic operations and every `ValueError` guard.

```bash
# Mac/Linux
python3 test_calculator.py

# Windows
python test_calculator.py
```

Expected output:

```
Ran 14 tests in 0.000s

OK
```
