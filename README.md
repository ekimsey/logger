# Logger
Logger is a simple logging module for Python 3.

## Required:
* Python 3.5 or newer

## Usage:
1. Copy the logger project folder into your Python 3 project.
2. Import the logger module: `from logger import logger`
3. Call logger's log_message method: `logger.log_message(0, "ERROR message")`

### Parameters
*Input parameter* | *Type* | *Description*
--|--|--
level | int | Severity level of message: '0' for exception, '1' for debug.
message | str | Message to be written to the log file.

*Output parameter* | *Type* | *Description*
--|--|--
N/A | None | Nothing