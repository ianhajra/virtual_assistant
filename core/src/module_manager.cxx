#include "../include/module_manager.h"

ModManager::ModManager()
    : logger_(nullptr)
{
}

ModManager::ModManager(Logger &logger)
    : logger_(&logger) // Initialize the logger reference
{
    this->logger_->log(LogLevel::INFO, "ModManager initialized");
}

ModManager::~ModManager()
{
    
}