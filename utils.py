def configure_qr():
    colors = [
        "black", "white", "blue", "red", "green",
        "teal", "purple", "orange", "yellow", "gray",
        "transparent"
    ]

    def choose_color(prompt, allow_transparent=False):
        print(f"\n{prompt}")
        for i, color in enumerate(colors):
            if not allow_transparent and color == "transparent":
                continue
            print(f"{i + 1}. {color}")
        
        while True:
            choice = input("Choose number: ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(colors):
                    selected = colors[index]
                    if not allow_transparent and selected == "transparent":
                        print("Transparent background not allowed here.")
                    else:
                        return selected
            print("Invalid choice. Please try again.")

    def choose_format():
        formats = ["png", "jpg", "svg"]
        print("\nChoose output format:")
        for i, fmt in enumerate(formats):
            print(f"{i + 1}. {fmt}")
        while True:
            choice = input("Choose number: ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(formats):
                    return formats[index]
            print("Invalid choice. Please choose again.")

    fill = choose_color("Choose foreground color (fill):")
    background = choose_color("Choose background color:", allow_transparent=True)
    output_format = choose_format()

    return {
        "fill": fill,
        "background": background,
        "format": output_format
    }
