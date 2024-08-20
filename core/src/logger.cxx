#include "../include/logger.h"
#include "../include/utils.h"
#include <iostream>
#include <ctime>

// Constructor: Opens the log file
Logger::Logger(const std::string& filename)
{
    logFile.open(filename, std::ios::app);
    if (!logFile) {
        std::cerr << "Error: Could not open log file: " << filename << std::endl;
    }
}

// Destructor: Closes the log file
Logger::~Logger()
{
    if (logFile.is_open()) {
        logFile.close();
    }
}

// Convert log level to string
std::string Logger::levelToString(LogLevel level)
{
    switch (level) {
        case LogLevel::DEBUG: return "DEBUG";
        case LogLevel::WARNING: return "WARNING";
        case LogLevel::ERROR: return "ERROR";
        default: return "UNKNOWN";
    }
}

// Log a message with a given log level
void Logger::log(LogLevel level, const std::string& message)
{
    logMessage(levelToString(level), message);
}

// Convenience methods for specific log levels
void Logger::logDebug(const std::string& message)
{
    log(LogLevel::DEBUG, message);
}

void Logger::logWarning(const std::string& message)
{
    log(LogLevel::WARNING, message);
}

void Logger::logError(const std::string& message)
{
    log(LogLevel::ERROR, message);
}

// Log the message with the appropriate formatting
void Logger::logMessage(const std::string& levelStr, const std::string& message)
{
    std::time_t now = std::time(nullptr);
    std::string timeStr = std::asctime(std::localtime(&now));
    timeStr.pop_back(); // Remove the newline character from the end of the time string

    std::string formattedMessage = "[" + timeStr + "] [" + levelStr + "] " + message;

    if (logFile.is_open()) {
        logFile << formattedMessage << std::endl;
    }

    // Optional: Also print the log message to the console
    std::cout << formattedMessage << std::endl;
}
