# Define compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Icore/include
LDFLAGS = 

# Directory variables
SRC_DIR = core/src
OBJ_DIR = obj
BIN_DIR = bin

# List of source files
SRC = $(wildcard $(SRC_DIR)/*.cxx)
# Corresponding object files
OBJ = $(patsubst $(SRC_DIR)/%.cxx,$(OBJ_DIR)/%.o,$(SRC))

# Target executable
TARGET = $(BIN_DIR)/virtual_assistant

# Default target
all: $(TARGET) print

# Link the object files to create the main executable
$(TARGET): $(OBJ)
	@mkdir -p $(BIN_DIR)
	$(CXX) $(LDFLAGS) -o $@ $^

# Compile the source files into object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cxx
	@mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build artifacts
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

# auto run after build
auto:
	make clean all
	./$(TARGET)

# Phony targets
.PHONY: all clean print