import pytest
from nlp.text_processing import normalize, tokenize, remove_stop_words, stem, process_text

# normalize text by converting it to lowercase and removing non alphabetic and whitespace characters
def test_normalize():
    assert normalize("Hello, World!") == "hello world"
    assert normalize("WeIrD InPUt") == "weird input"
    assert normalize("ALL CAPS INPUT") == "all caps input"
    assert normalize("all lowercase input") == "all lowercase input"
    assert normalize("572983758923789327") == ""
    assert normalize("@%^&^$#") == ""
    assert normalize("HELLO") == "hello"
    assert normalize("HeLLo WoRLd") == "hello world"
    assert normalize("123ABCdef") == "abcdef"
    assert normalize("!@#$%^&*()_+{}:<>? ABCD") == " abcd"
    assert normalize("ÀÉÎÕÛ") == ""
    assert normalize("") == ""
    assert normalize("Hello\nWorld") == "hello\nworld"
    assert normalize("Hello\tWorld") == "hello\tworld"
    assert normalize("  HeLLo  WoRLd  ") == "  hello  world  "
    assert normalize("你好世界HELLO") == "hello"
    assert normalize("THIS IS A TEST") == "this is a test"
    assert normalize("python CODE") == "python code"
    assert normalize("12345") == ""
    assert normalize("MixedCASE123") == "mixedcase"
    assert normalize("Leading and Trailing Spaces    ") == "leading and trailing spaces    "
    assert normalize("    ALL SPACES IN FRONT") == "    all spaces in front"
    assert normalize("SpecialCharacters!@#") == "specialcharacters"
    assert normalize("CamelCaseWord") == "camelcaseword"
    assert normalize("UPPERCASE123lower") == "uppercaselower"
    assert normalize("numbers1234567890") == "numbers"
    assert normalize("    SPACES everywhere  ") == "    spaces everywhere  "
    assert normalize("String with Tabs\t and Newlines\n") == "string with tabs\t and newlines\n"
    assert normalize("UPPER AND lower") == "upper and lower"
    assert normalize("123 Mixed Upper LOWER!") == " mixed upper lower"
    assert normalize("Ümläüts ShÖuld BE lowER") == "mlts shuld be lower"
    assert normalize("LONG STRING OF TEXT TO TEST THE FUNCTION") == "long string of text to test the function"
    assert normalize("SPACES\tTABS\nNEWLINES") == "spaces\ttabs\nnewlines"
    assert normalize("PYTHON\tROCKS") == "python\trocks"
    assert normalize("TextWith123AndSymbols!@#") == "textwithandsymbols"
    assert normalize("lowercase remains unchanged") == "lowercase remains unchanged"
    assert normalize("Hello World!123") == "hello world"
    assert normalize("Text\n\nWith\n\nNewlines") == "text\n\nwith\n\nnewlines"
    assert normalize("Multiple!@#$%^&*() Symbols") == "multiple symbols"
    assert normalize("Whitespace\t\t\t and Newline\n\n\n") == "whitespace\t\t\t and newline\n\n\n"
    assert normalize("   Leading Spaces Only   ") == "   leading spaces only   "
    assert normalize("Special_characters_are_removed!") == "specialcharactersareremoved"
    assert normalize("Hello---World!!!") == "helloworld"
    assert normalize("1234\n5678\n") == "\n\n"
    assert normalize("Mixed_Characters123") == "mixedcharacters"
    assert normalize("End_Of_String!!!") == "endofstring"
    assert normalize("A**Test") == "atest"
    assert normalize("Another_Test@Example") == "anothertestexample"
    assert normalize("Trailing___Underscores___") == "trailingunderscores"
    assert normalize("Larger\nBlock\nOf\nText") == "larger\nblock\nof\ntext"

# tokenize the text, splitting it into individual words or tokens
def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]
    assert tokenize("  leading spaces") == ["leading", "spaces"]
    assert tokenize("trailing spaces  ") == ["trailing", "spaces"]
    assert tokenize("multiple   spaces") == ["multiple", "spaces"]
    assert tokenize("tabs and spaces") == ["tabs", "and", "spaces"]
    assert tokenize("newlines in text") == ["newlines", "in", "text"]
    assert tokenize("mixed   spaces") == ["mixed", "spaces"]
    assert tokenize("words with numbers") == ["words", "with", "numbers"]
    assert tokenize("special characters") == ["special", "characters"]
    assert tokenize("camelcase words") == ["camelcase", "words"]
    assert tokenize("upper lower case") == ["upper", "lower", "case"]
    assert tokenize("numbers") == ["numbers"]  
    assert tokenize("leading multiple spaces") == ["leading", "multiple", "spaces"]
    assert tokenize("trailing multiple spaces") == ["trailing", "multiple", "spaces"]
    assert tokenize("tabs at the start") == ["tabs", "at", "the", "start"]
    assert tokenize("end with tabs") == ["end", "with", "tabs"]
    assert tokenize("newlines at start") == ["newlines", "at", "start"]
    assert tokenize("end with newlines") == ["end", "with", "newlines"]
    assert tokenize("mixed whitespace characters") == ["mixed", "whitespace", "characters"]
    assert tokenize("singleword") == ["singleword"]
    assert tokenize("two words") == ["two", "words"]
    assert tokenize("three words here") == ["three", "words", "here"]
    assert tokenize("a sentence with punctuation") == ["a", "sentence", "with", "punctuation"]
    assert tokenize("mixed leading and trailing") == ["mixed", "leading", "and", "trailing"]
    assert tokenize("") == []
    assert tokenize(" ") == []
    assert tokenize("\t") == []
    assert tokenize("\n") == []
    assert tokenize("wordswithhyphens") == ["wordswithhyphens"]
    assert tokenize("words_with_underscores") == ["words_with_underscores"]

# remove common stop words from a list of tokens
# (e.g., "and", "the", "is", etc.)
def test_remove_stop_words():
    assert remove_stop_words(["i", "am", "going", "to", "the", "store"]) == ["going", "store"]
    assert remove_stop_words(["a", "the", "is", "in", "on"]) == []
    assert remove_stop_words(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
    assert remove_stop_words(["the", "quick", "Brown", "fox"]) == ["quick", "Brown", "fox"]
    assert remove_stop_words([]) == []
    assert remove_stop_words(["can't", "won't", "he", "said", "she"]) == ["said"]
    assert remove_stop_words(["an", "about", "hello", "there"]) == ["hello"]
    assert remove_stop_words(["can't", "won't", "why", "hello"]) == ["hello"]
    assert remove_stop_words(["here", "is", "another", "test"]) == ["here", "another", "test"]
    assert remove_stop_words(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]) == ["quick", "brown", "fox", "jumps", "lazy", "dog"]
    assert remove_stop_words(["what", "is", "the", "meaning", "of", "life"]) == ["meaning", "life"]
    assert remove_stop_words(["this", "is", "a", "test", "with", "multiple", "stop", "words"]) == ["test", "multiple", "stop", "words"]
    assert remove_stop_words(["how", "are", "you", "doing", "today"]) == ["today"]
    assert remove_stop_words(["i", "have", "been", "working", "hard"]) == ["working", "hard"]
    assert remove_stop_words(["through", "the", "night", "and", "day"]) == ["night", "day"]
    assert remove_stop_words(["stop", "words", "are", "important", "for", "text", "processing"]) == ["stop", "words", "important", "text", "processing"]
    assert remove_stop_words(["all", "words", "should", "be", "processed"]) == ["words", "processed"]
    assert remove_stop_words(["a", "little", "bit", "of", "space", "here"]) == ["little", "bit", "space", "here"]
    assert remove_stop_words(["these", "are", "some", "random", "words"]) == ["random", "words"]
    assert remove_stop_words(["even", "if", "the", "stop", "words", "are", "complex"]) == ["even", "stop", "words", "complex"]
    assert remove_stop_words(["can", "you", "see", "the", "difference"]) == ["see", "difference"]
    assert remove_stop_words(["removing", "stop", "words", "improves", "clarity"]) == ["removing", "stop", "words", "improves", "clarity"]
    assert remove_stop_words(["here", "is", "another", "sentence", "with", "stop", "words"]) == ["here", "another", "sentence", "stop", "words"]
    assert remove_stop_words(["simple", "text", "processing", "examples"]) == ["simple", "text", "processing", "examples"]
    assert remove_stop_words(["test", "cases", "should", "cover", "all", "edge", "cases"]) == ["test", "cases", "cover", "edge", "cases"]
    assert remove_stop_words(["the", "more", "tests", "you", "write", "the", "better"]) == ["tests", "write", "better"]
    assert remove_stop_words(["make", "sure", "to", "test", "edge", "cases", "thoroughly"]) == ["make", "sure", "test", "edge", "cases", "thoroughly"]
    
# Checking that words properly reduce to stemmed format
def test_stem():
    assert stem(["running"]) == ["run"]
    assert stem(["jumps"]) == ["jump"]
    assert stem(["easily"]) == ["easili"]
    assert stem(["flying"]) == ["fli"]
    assert stem(["cats"]) == ["cat"]
    assert stem(["knives"]) == ["knive"]
    assert stem(["better"]) == ["better"]
    assert stem(["happily"]) == ["happili"]
    assert stem(["happiness"]) == ["happi"]
    assert stem(["studying"]) == ["studi"]
    assert stem(["studies"]) == ["studi"]
    assert stem(["studied"]) == ["studi"]
    assert stem(["argue"]) == ["argu"]
    assert stem(["argued"]) == ["argu"]
    assert stem(["argues"]) == ["argu"]
    assert stem(["arguing"]) == ["argu"]
    assert stem(["relational"]) == ["relat"]
    assert stem(["relationally"]) == ["relat"]
    assert stem(["relationalize"]) == ["relation"]
    assert stem(["driving"]) == ["drive"]
    assert stem(["driver"]) == ["driver"]
    assert stem(["drivers"]) == ["driver"]
    assert stem(["denied"]) == ["deni"]
    assert stem(["denies"]) == ["deni"]
    assert stem(["denying"]) == ["deni"]
    assert stem(["dancer"]) == ["dancer"]
    assert stem(["dancing"]) == ["danc"]
    assert stem(["dances"]) == ["danc"]
    assert stem(["hoped"]) == ["hope"]
    assert stem(["hoping"]) == ["hope"]
    assert stem(["hopes"]) == ["hope"]
    assert stem(["flies"]) == ["fli"]
    assert stem(["cries"]) == ["cri"]
    assert stem(["crying"]) == ["cri"]
    assert stem(["tried"]) == ["tri"]
    assert stem(["tries"]) == ["tri"]
    assert stem(["trying"]) == ["tri"]
    assert stem(["playing"]) == ["play"]
    assert stem(["plays"]) == ["play"]
    assert stem(["played"]) == ["play"]
    assert stem(["saying"]) == ["say"]
    assert stem(["says"]) == ["say"]
    assert stem(["said"]) == ["said"]
    assert stem(["running", "jumps"]) == ["run", "jump"]
    assert stem(["cats", "dogs"]) == ["cat", "dog"]
    assert stem(["happily", "quickly"]) == ["happili", "quickli"]
    assert stem([]) == []
    assert stem([""]) == [""]
    assert stem(["hello", "world"]) == ["hello", "world"]
    
# Checking end-to-end functionality of the text_processing functions
def test_process_text():
    assert process_text("Hello, World!") == ["hello", "world"]
    assert process_text("WeIrD InPUt") == ["weird", "input"]
    assert process_text("ALL CAPS INPUT") == ["all", "caps", "input"]
    assert process_text("all lowercase input") == ["all", "lowercase", "input"]
    assert process_text("572983758923789327") == []
    assert process_text("@%^&^$#") == []
    assert process_text("HELLO") == ["hello"]
    assert process_text("HeLLo WoRLd") == ["hello", "world"]
    assert process_text("123ABCdef") == ["abcdef"]
    assert process_text("!@#$%^&*()_+{}:<>? ABCD") == ["abcd"]
    assert process_text("ÀÉÎÕÛ") == []
    assert process_text("") == []
    assert process_text("Hello\nWorld") == ["hello", "world"]
    assert process_text("Hello\tWorld") == ["hello", "world"]
    assert process_text("  HeLLo  WoRLd  ") == ["hello", "world"]
    assert process_text("你好世界HELLO") == ["hello"]
    assert process_text("THIS IS A TEST") == ["this", "test"]
    assert process_text("python CODE") == ["python", "code"]
    assert process_text("12345") == []
    assert process_text("MixedCASE123") == ["mixedcase"]
    assert process_text("Leading and Trailing Spaces    ") == ["leading", "trailing", "spaces"]
    assert process_text("    ALL SPACES IN FRONT") == ["all", "spaces", "front"]
    assert process_text("SpecialCharacters!@#") == ["specialcharacters"]
    assert process_text("CamelCaseWord") == ["camelcaseword"]
    assert process_text("UPPERCASE123lower") == ["uppercaselower"]
    assert process_text("numbers1234567890") == ["numbers"]
    assert process_text("    SPACES everywhere  ") == ["spaces", "everywhere"]
    assert process_text("String with Tabs\t and Newlines\n") == ["string", "tabs", "newlines"]
    assert process_text("UPPER AND lower") == ["upper", "lower"]
    assert process_text("123 Mixed Upper LOWER!") == ["mixed", "upper", "lower"]
    assert process_text("Ümläüts ShÖuld BE lowER") == ["mlts", "shuld", "lower"]
    assert process_text("LONG STRING OF TEXT TO TEST THE FUNCTION") == ["long", "string", "text", "test", "function"]
    assert process_text("SPACES\tTABS\nNEWLINES") == ["spaces", "tabs", "newlines"]
    assert process_text("PYTHON\tROCKS") == ["python", "rocks"]
    assert process_text("TextWith123AndSymbols!@#") == ["textwithandsymbols"]
    assert process_text("lowercase remains unchanged") == ["lowercase", "remains", "unchanged"]
    assert process_text("Hello World!123") == ["hello", "world"]
    assert process_text("Text\n\nWith\n\nNewlines") == ["text", "with", "newlines"]
    assert process_text("Multiple!@#$%^&*() Symbols") == ["multiple", "symbols"]
    assert process_text("Whitespace\t\t\t and Newline\n\n\n") == ["whitespace", "and", "newline"]
    assert process_text("   Leading Spaces Only   ") == ["leading", "spaces", "only"]
    assert process_text("Special_characters_are_removed!") == ["specialcharactersareremoved"]
    assert process_text("Hello---World!!!") == ["helloworld"]
    assert process_text("1234\n5678\n") == []
    assert process_text("Mixed_Characters123") == ["mixedcharacters"]
    assert process_text("End_Of_String!!!") == ["endofstring"]
    assert process_text("A**Test") == ["atest"]
    assert process_text("Another_Test@Example") == ["anothertestexample"]
    assert process_text("Trailing___Underscores___") == ["trailingunderscores"]
    assert process_text("Larger\nBlock\nOf\nText") == ["larger", "block", "of", "text"]
