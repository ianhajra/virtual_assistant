#pragma once

#include <string>
#include <fstream>

enum class LogLevel {
    DEBUG,
    WARNING,
    ERROR
};

class Logger
{
public:
    // Default constructor: Initialize with a default filename
    Logger();

    // Constructor: Takes a filename for the log file
    explicit Logger(const std::string& filename);

    // Destructor: Closes the log file
    ~Logger();

    // Delete copy constructor and copy assignment operator
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    // Allow move construction and move assignment
    Logger(Logger&& other) noexcept;
    Logger& operator=(Logger&& other) noexcept;

    void log(LogLevel level, const std::string& message);

    void logDebug(const std::string& message);
    void logWarning(const std::string& message);
    void logError(const std::string& message);

private:
    std::ofstream logFile;
    std::string levelToString(LogLevel level);
    void logMessage(const std::string& levelStr, const std::string& message);
    void initializeDefaultLogFile(); // Initialize with a default filename
};
