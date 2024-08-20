#ifndef ENGINE_H
#define ENGINE_H

#include "../include/config_loader.h"
#include "../include/logger.h"
#include "../include/module_manager.h"
#include "../include/utils.h"

class Engine
{
public:
    Engine();

    ~Engine();

    void init();

    void run();

private:
    ModManager modManager;
};

#endif // ENGINE_H