#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/utils.h"
#include "../include/json.hpp"
#include <fstream>
#include <iostream>
using json = nlohmann::json;

ConfigLoader::ConfigLoader()
{

}

ConfigLoader::~ConfigLoader()
{

}
 
ConfigLoader::ConfigLoader(std::string &file_path, Logger& logger){   
    std::ifstream config_file;
    config_file.open(file_path);
    if (!config_file.is_open())
    {   
        logger.log(LogLevel::WARNING, "Could not open config file at: " + file_path);
        logger.log(LogLevel::WARNING, "Creating new config file at: " + file_path);

        std::ofstream new_config_file(file_path);
        new_config_file << "{\n \"name\": \"DEFAULT NAME\" \n}" << std::endl;
        new_config_file.close();
        config_file.open(file_path);
    }
    else {
        logger.log(LogLevel::INFO, "Opened config file at: " + file_path);
    }

    readConfig(config_file);

    logger.log(LogLevel::INFO, "ConfigLoader Initialized");
}


void ConfigLoader::readConfig(std::ifstream &config_file){
    // This takes the user_config member variable and gives it all the info
    // from the json file. It works as an STL container. 
    this->user_config = json::parse(config_file);
    std::cout << this->user_config["name"] << std::endl;
}

ConfigLoader& ConfigLoader::operator=(ConfigLoader&& other)
{
    this->user_config = std::move(other.user_config);
    return *this;
}