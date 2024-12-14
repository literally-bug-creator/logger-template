# Root Logger Template (Python Logging) 📜🛠️

A simple and convenient template for setting up a logger using `logging.root`, which outputs messages to both the console and a file. Easy to integrate into any project.

## Key Features 🌟:
- **Console Output** with configurable log levels (INFO, DEBUG, WARNING, ERROR).
- **File Logging** for saving logs (with customizable log level).
- **RotatingFileHandler**: Automatically rotates log files when they reach a specified size, ensuring logs don't get too large. 📂🔄
- **TimedRotatingFileHandler**: Automatically rotates log files at a set interval (e.g., daily, weekly), ideal for time-based log management. 🕰️📂
- **Dynamic Configuration**: Log settings are dynamically loaded from `.env.logger` using `pydantic_settings`. 🎛️

## How to Use 🔧:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/literally-bug-creator/logger-template.git
    cd logger-template
    ```

2. **Create a `.env.logger` file** with your desired configuration:
    ```env
    LEVEL=0                 # Logging level (e.g., 0=NOTSET, 10=DEBUG, 20=INFO, etc.)
                            # See: https://docs.python.org/3/library/logging.html#logging-levels
    FILENAME="app.log"      # Path to the log file where logs will be saved.
                            # Documentation: https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler
    BACKUP_COUNT=4          # Number of backup files to keep for RotatingFileHandler.
                            # See: https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
    MAX_BYTES=102400        # Maximum size of the log file in bytes before rotation.
                            # Documentation: https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler
    ROTATING_INTERVAL=1     # Interval for timed rotations (e.g., 1 day, 1 week, etc.).
                            # See: https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
    ROTATING_PER="d"        # Unit of time for rotation: 's' (seconds), 'm' (minutes), 'h' (hours), or 'd' (days).
                            # Documentation: https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
    ```

3. **Import your root logger**:
    ```python
    from logger import root_logger
    ```

4. **Create a logger instance** using `root_logger.getLogger(*logger_name*)`:
    ```python
    logger = root_logger.getLogger(__name__)
    ```

5. **Use the logger**:
    ```python
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    ```

Logs will be shown in the console and saved to the `app.log` file 📂.

## Installation 📦:
Simply download or clone the repository and use it as part of your project. The logger will automatically pick up settings from `.env.logger`.

## Additional Notes 📝:
- Ensure your `.env.logger` file is in the root directory of your project or properly configured for `pydantic_settings` to locate it.
- This template provides flexibility for managing log levels and file handling dynamically.
