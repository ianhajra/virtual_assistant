#pragma once
#include <fstream>
#include <string>

class ConfigLoader
{
public:
    ConfigLoader(std::string &file_path, Logger& logger);

    ~ConfigLoader();

    ConfigLoader& operator=(ConfigLoader&& other);

    ConfigLoader init(std::string &file_path, Logger& logger);

private:
    config user_config;
    std::ifstream config_file;
};