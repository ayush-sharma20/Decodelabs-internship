def run_logic_engine():
    print("======================================================")
    print("  DECODELABS DETERMINISTIC LOGIC ENGINE [PROJECT 1]   ")
    print("======================================================\n")

    while True:
        # Phase 1: Input & Sanitization
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # Phase 2 & 3: Process Logic & Output Generation
        if clean_input in ['exit', 'quit', 'bye', 'goodbye']:
            print("System: Safe loop termination complete. Goodbye!")
            break
        elif clean_input in ['hello', 'hi', 'hey']:
            print("Chatbot: Hello! I am a deterministic 'White Box' system.")
        elif 'project 1' in clean_input or 'decodelabs' in clean_input:
            print("Chatbot: Project 1 focuses on mastering Control Flow and Input Normalization.")
        else:
            print("Chatbot: Input unrecognized. Please use standard commands.")
            
        print("-" * 50)

if  __name__ == "_main_":
    run_logic_engine()
