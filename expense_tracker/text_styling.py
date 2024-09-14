class Colors:
    Reset = '\033[0m'
    Blue = '\033[94m'
    Red = '\033[91m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Green = '\033[92m'
    Cyan = '\033[96m'

    def colored_text(text, color):
        colors = {
            'blue': Colors.Blue,
            'red': Colors.Red,
            'yellow': Colors.Yellow,
            'magenta': Colors.Magenta,
            'green': Colors.Green,
            'cyan': Colors.Cyan,
        }

        reset_color = Colors.Reset  # Reset color to default

        if color in colors:
            return f"{colors[color]}{text}{reset_color}"
        else:
            return f"Invalid color: {text}"
