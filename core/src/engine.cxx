#include "../include/engine.h"
#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/module_manager.h"
#include "../include/utils.h"

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
}

void Engine::run()
{
}