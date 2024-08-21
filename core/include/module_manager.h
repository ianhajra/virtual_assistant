#pragma once
#include "../include/logger.h"

class ModManager
{
public:
    ModManager(); // Default constructor

    explicit ModManager(Logger& logger); // Parameterized constructor

    ~ModManager();

private:
    Logger* logger_; // Use a pointer to allow optional initialization
};
