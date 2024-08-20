#include "../include/engine.h"
#include <filesystem>

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
    this->utils = Utils();

    std::string logDir = "../../log";
    std::string logFile = logDir + "/engine_log.txt";
    std::filesystem::create_directories(logDir);
    this->logger = Logger(logFile);

    this->configLoader = ConfigLoader();
    
    this->modManager = ModManager();
}

void Engine::run()
{
}