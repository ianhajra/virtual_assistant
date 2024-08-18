def test_normalize():
  return False

def test_tokenize():
  return False

def test_remove_punctuation():
  return False

def test_remove_stop_words():
  return False

def test_lemmatize():
  return False

def test_process_command():
  return False


# Test output
if(not test_normalize()):
  print("Test normalize failed")

if(not test_tokenize()):
  print("Test tokenize failed")

if(not test_remove_punctuation()):
  print("Test remove_punctuation failed")

if(not test_remove_stop_words()):
  print("Test remove_stop_words failed")

if(not test_lemmatize()):
  print("Test lemmatize failed")

if(not test_process_command()):
  print("Test process_command failed")

  
  
