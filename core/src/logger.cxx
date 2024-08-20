#include "../include/logger.h"
#include "../include/utils.h"
#include <iostream>
#include <ctime>

// Define ANSI color codes
const std::string RESET = "\033[0m";
const std::string BLUE = "\033[34m";
const std::string YELLOW = "\033[33m";
const std::string RED = "\033[31m";

// Default constructor: Initialize with a default filename
Logger::Logger()
{
    initializeDefaultLogFile();
}

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

// Move constructor
Logger::Logger(Logger&& other) noexcept
    : logFile(std::move(other.logFile))
{
}

// Move assignment operator
Logger& Logger::operator=(Logger&& other) noexcept
{
    if (this != &other) {
        if (logFile.is_open()) {
            logFile.close();
        }
        logFile = std::move(other.logFile);
    }
    return *this;
}

// Initialize with a default filename
void Logger::initializeDefaultLogFile()
{
    logFile.open("log/default_log.txt", std::ios::app);
    if (!logFile) {
        std::cerr << "Error: Could not open default log file" << std::endl;
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
    logMessage(level, message);
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
void Logger::logMessage(LogLevel level, const std::string& message)
{
    std::time_t now = std::time(nullptr);
    std::string timeStr = std::asctime(std::localtime(&now));
    timeStr.pop_back(); // Remove the newline character from the end of the time string

    std::string levelStr = levelToString(level);
    std::string color;

    switch (level) {
        case LogLevel::DEBUG: color = BLUE; break;
        case LogLevel::WARNING: color = YELLOW; break;
        case LogLevel::ERROR: color = RED; break;
    }

    std::string formattedMessage = "[" + timeStr + "] [" + color + levelStr + RESET + "] " + message;

    if (logFile.is_open()) {
        logFile << formattedMessage << std::endl;
    }

    // Print the log message to the console
    std::cout << formattedMessage << std::endl;
}
