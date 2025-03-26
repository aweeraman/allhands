#!/usr/bin/env python3
"""
A simple CLI application using Textual framework.
Implements /hello and /exit commands.
"""

from textual.app import App, ComposeResult
from textual.widgets import Input, RichLog
from textual.containers import Container
from textual import events


class TextualCLI(App):
    """A simple CLI application with command support."""

    CSS = """
    Container {
        layout: vertical;
        height: 100%;
        width: 100%;
    }
    
    RichLog {
        height: 1fr;
        background: $surface;
        color: $text;
        border: solid $primary;
        padding: 1;
    }
    
    Input {
        dock: bottom;
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with Container():
            yield RichLog(id="log")
            yield Input(placeholder="Type a command (e.g. /hello, /exit)", id="command_input")

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        log = self.query_one("#log", RichLog)
        log.write("Welcome to TextualCLI!")
        log.write("Available commands:")
        log.write("  /hello - Display a greeting")
        log.write("  /exit  - Exit the application")
        log.write("\nType a command and press Enter.")
        
        # Focus the input field
        self.query_one("#command_input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Called when the user submits the input."""
        command = event.value.strip()
        log = self.query_one("#log", RichLog)
        
        # Log the command
        log.write(f"> {command}")
        
        # Process commands
        if command == "/hello":
            log.write("Hello, world! 👋")
        elif command == "/exit":
            log.write("Exiting application...")
            self.exit()
        elif command.startswith("/"):
            log.write(f"Unknown command: {command}")
        else:
            log.write("Not a command. Commands start with '/'")
        
        # Clear the input field
        event.input.value = ""


if __name__ == "__main__":
    app = TextualCLI()
    app.run()