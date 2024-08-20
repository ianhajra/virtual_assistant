#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/utils.h"
#include <fstream>
#include <iostream>

ConfigLoader::ConfigLoader()
{
    
}

ConfigLoader::ConfigLoader(std::string &file_path, Logger& logger)
{   
    this->config_file.open(file_path);
    if (!this->config_file.is_open())
    {   
        logger.log(LogLevel::ERROR, "Error: Could not open config file: " + file_path);
    }
}


ConfigLoader::~ConfigLoader()
{
    
}

ConfigLoader& ConfigLoader::operator=(ConfigLoader&& other)
{
    this->config_file = std::move(other.config_file);
    this->user_config = std::move(other.user_config);
    return *this;
}