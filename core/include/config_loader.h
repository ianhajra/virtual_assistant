#ifndef CONFIG_LOADER_H
#define CONFIG_LOADER_H

#include <string>
#include <fstream>
#include "../include/json.hpp"

class Logger; // Forward declaration of Logger

class ConfigLoader {
public:
    ConfigLoader();
    ConfigLoader(std::string &file_path, Logger& logger);
    ~ConfigLoader();

    ConfigLoader& operator=(ConfigLoader&& other);

    void readConfig();

private:
    nlohmann::json user_config;
};

#endif // CONFIG_LOADER_H