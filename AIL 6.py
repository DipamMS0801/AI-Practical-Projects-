def bookstore_bot():
    print("[] Welcome to BookStoreBot!")
    print("How can I help you today?")
    print("Type 'help' to see available options.")

    while True:
        user_input = input("\nYou: ").lower()

        if 'help' in user_input:
            print("\nI can assist with the following:")
            print("- Book search")
            print("- Order tracking")
            print("- Delivery information")
            print("- Return policy")
            print("- Payment methods")
            print("Type 'exit' to end the chat.")

        elif 'book' in user_input or 'find' in user_input or 'search' in user_input:
            title = input("Please enter the book title or keyword: ")
            print(f"Searching for books related to '{title}'... []")
            print("Here are some matching results (mock):\n1. Learn Python\n2. Python for Beginners\n3. Advanced Python Coding")

        elif 'track' in user_input or 'order' in user_input:
            order_id = input("Please enter your Order ID: ")
            print(f"Tracking order {order_id}...")
            print("Your order is out for delivery and will arrive in 2 days.")

        elif 'delivery' in user_input or 'shipping' in user_input:
            print("We offer FREE delivery on orders over $25.")
            print("For orders below $25, a small fee of $3.99 applies.")

        elif 'return' in user_input:
            print("You can return any book within 7 days if it's unused and undamaged.")
            print("Visit your orders page and click 'Return' to start the process.")

        elif 'payment' in user_input:
            print("We accept the following payment methods:")
            print("- Credit/Debit Cards\n- PayPal\n- Apple Pay\n- Google Pay")

        elif 'exit' in user_input or 'bye' in user_input:
            print("Thank you for visiting BookStoreBot! Have a great day! []")
            break

        else:
            print("Sorry, I didn't understand that. Please type 'help' to see what I can do.")

# Run the chatbot
bookstore_bot()