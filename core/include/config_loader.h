#ifndef CONFIG_LOADER_H
#define CONFIG_LOADER_H

#include <string>
#include <fstream>

class Logger; // Forward declaration of Logger

struct config {
    std::string name;
};

class ConfigLoader {
public:
    ConfigLoader();
    ConfigLoader(std::string &file_path, Logger& logger);
    ~ConfigLoader();

    ConfigLoader& operator=(ConfigLoader&& other);

private:
    void init(const std::string &file_path, Logger& logger);
    config user_config;
    std::ifstream config_file;
};

#endif // CONFIG_LOADER_H