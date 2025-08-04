# `UV`: A Fast Python Package and Script Manager

The `uv` tool is a modern Python package manager and project runner designed for speed, simplicity, and efficiency. It simplifies the management of virtual environments, dependencies, and script execution—especially useful when working across platforms, including WSL (Windows Subsystem for Linux).

Below is a quick guide to help you get started with `uv`, whether you're creating a full project or just running standalone scripts.

---

## 🌱 Starting a New Project

To initialize a new Python project using `uv`, run:

```sh
uv init chau-code
```

This will set up a default project structure with essential files:

* `.python-version` – Specifies the Python version for the environment
* `main.py` – Your main Python entry point
* `pyproject.toml` – Project metadata and dependency definitions

A virtual environment (`.venv`) will also be created, along with a `uv.lock` file to track your exact dependency versions.

Project Structure Example:

```
chau-code/
├── .venv/
├── main.py
├── pyproject.toml
├── uv.lock
└── .python-version
```

---

## 🚀 Running the Project

Once your project is set up, you can run your main script with:

```sh
uv run main.py
```

This ensures the script runs in the isolated `.venv` environment with all dependencies properly loaded.

---

## 📦 Adding Dependencies

To add packages to your project, use:

```sh
uv add fastapi
```

This will update both the `pyproject.toml` and `uv.lock` files, ensuring reproducibility across systems.

---

## 📦 Distributing Your Project (e.g., for WSL or other environments)

When you're ready to distribute your project, use:

```sh
uv build
```

This compiles your source and environment into a distributable format, making it easy to move between machines or platforms.

---

## ❓ Finding Help

To get a list of all available `uv` commands and usage help, simply run:

```sh
uv
```

This will display command-line options, subcommands, and usage tips.

---

## 🧪 Running Standalone Scripts with Dependencies

You don’t always need to create a full project. `uv` also supports script-based workflows.

### Run a Script with Temporary Dependencies

If you want to run a script using some packages without installing them globally or setting up a full environment:

```sh
uv run --with "flask" --with "requests" scripteg.py
```

### Adding Dependencies to a Script Permanently

If your script’s dependencies grow, you can define them with:

```sh
uv add --script scripteg.py "flask" "requests"
```

This way, `uv` can manage the script’s dependencies consistently across environments.

---

## 🔚 Conclusion

`uv` is a powerful tool for Python developers who want speed and flexibility without the overhead of traditional virtual environment management tools. Whether you're working on a full-stack FastAPI app or a small automation script, `uv` can help streamline your development process.

> **Tip:** Check the official documentation or run `uv` in your terminal to explore more features.
