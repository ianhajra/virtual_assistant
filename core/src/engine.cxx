#include "../include/engine.h"
#include <filesystem>
#include <iostream>

/**
 * This constructor will initialize all of the appropriate classes
 * and will then proceed to begin running
 */
Engine::Engine()
{
    this->init();
    this->run();
}

Engine::~Engine()
{
    // empty destructor for now
}

/**
 * Function used to initialize the engine. It will create the following:
 *   - utils
 *   - a logger
 *   - a config_loader
 *   - a module_manaer
 */
void Engine::init()
{   
    // Utils Initialization
    this->utils = Utils();

    // Logger Initialization
    std::string logDir = "../../log";
    std::string logFile = logDir + "/engine_log.txt";
    std::filesystem::create_directories(logDir);
    this->logger = Logger(logFile);
    
    // Config Loader Initialization
    std::string configDir = "../../user_information/";
    std::string configFile = configDir + "config.txt";
    std::filesystem::create_directories(configDir);
    this->configLoader = ConfigLoader(configFile, this->logger);

    // Module Manager Initialization
    this->modManager = ModManager();
}

void Engine::run()
{
    std::cout << "The engine can run!" << std::endl;
}