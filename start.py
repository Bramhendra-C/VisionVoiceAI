def menu():
    print("1. Run Face Detection")
    print("2. Get Face Unfocus Count")
    print("3. Voice assistant")
    print("4. Exit")

while True:
    menu()
    choice = input("Select an option: ")
    if choice == '1':
        import face
        face.run_face_detection()
    elif choice == '2':
        import face
        face.get_face_unfocus_count()
    elif choice == '3':
        import voice_assistant
        voice_assistant.run_assistant()
    elif choice == '4':
        print("Exiting the program.")
        break
    else :
        print("Invalid choice. Please try again.")