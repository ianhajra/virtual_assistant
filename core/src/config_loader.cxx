#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/utils.h"
#include "../include/json.hpp"
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
        logger.log(LogLevel::WARNING, "Could not open config file at: " + file_path);
        logger.log(LogLevel::WARNING, "Creating new config file at: " + file_path);

        std::ofstream new_config_file(file_path);
        new_config_file << "John Smith" << std::endl;
        new_config_file.close();
        this->config_file.open(file_path);
    }
    else {
        logger.log(LogLevel::DEBUG, "Opened config file at: " + file_path);
    }

    readConfig();
}

ConfigLoader::~ConfigLoader()
{
    this->config_file.close();
}

void ConfigLoader::readConfig(){
    
}

ConfigLoader& ConfigLoader::operator=(ConfigLoader&& other)
{
    this->config_file = std::move(other.config_file);
    this->user_config = std::move(other.user_config);
    return *this;
}