#pragma once

#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/module_manager.h"
#include "../include/utils.h"
#include "../include/constants.h"

class Engine
{
public:
    Engine();

    ~Engine();

    void init();

    void run();

private:
    ModManager modManager;
    Utils utils;
    Logger logger;
    ConfigLoader configLoader;
};

