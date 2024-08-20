#pragma once

#include <string>
#include <fstream>

/**
 * LogLevel class used to determine what type of logging to do
 */
enum class LogLevel {
    DEBUG,
    WARNING,
    ERROR
};

/**
 * Updated Logger class to handle the appropriate methods that will be used
 * for logging throughout the virtual_assistant
 */
class Logger
{
public:
    Logger(const std::string& filename);
    ~Logger();

    void log(LogLevel level, const std::string& message);

    void logDebug(const std::string& message);
    void logWarning(const std::string& message);
    void logError(const std::string& message);

private:
    std::ofstream logFile;
    std::string levelToString(LogLevel level);
    void logMessage(const std::string& levelStr, const std::string& message);
};