"""
Gradio Web Interface for Batman & Alfred

This module implements the Gradio-based web interface for interacting with
the Batman & Alfred Multi-Agent Framework.
"""

import os
import logging
import gradio as gr

logger = logging.getLogger(__name__)

class BatmanAlfredUI:
    """
    Gradio-based user interface for the Batman & Alfred Multi-Agent Framework.
    Provides conversational and voice interaction capabilities.
    """
    
    def __init__(self, config=None):
        """
        Initialize the Gradio UI.
        
        Args:
            config: Configuration dictionary for the UI
        """
        self.config = config or {}
        self.title = self.config.get("title", "Batman & Alfred Multi-Agent Framework")
        self.theme = self.config.get("theme", gr.themes.Soft())
        self.app = None
        logger.info("Gradio UI initialized")
    
    def _process_message(self, message, history):
        """
        Process a user message and generate a response.
        
        Args:
            message: User message
            history: Conversation history
            
        Returns:
            Agent response
        """
        # This will be connected to the Alfred Prime coordinator
        logger.info(f"Processing message: {message}")
        return "I'm Alfred, your AI assistant. This is a placeholder response."
    
    def build_interface(self):
        """
        Build the Gradio interface with all components.
        
        Returns:
            Gradio interface
        """
        with gr.Blocks(title=self.title, theme=self.theme) as app:
            gr.Markdown(f"# {self.title}")
            gr.Markdown("Your AI assistant powered by a multi-agent framework")
            
            with gr.Tab("Chat"):
                chatbot = gr.Chatbot(height=400)
                msg = gr.Textbox(placeholder="Type your message here...", show_label=False)
                clear = gr.Button("Clear")
                
                msg.submit(
                    self._process_message,
                    [msg, chatbot],
                    [msg, chatbot]
                )
                clear.click(lambda: None, None, chatbot, queue=False)
            
            with gr.Tab("Voice"):
                audio_input = gr.Audio(source="microphone", type="filepath")
                audio_output = gr.Audio(label="Response")
                
                audio_input.change(
                    lambda x: "voice_response_placeholder.wav",  # Will be implemented later
                    inputs=audio_input,
                    outputs=audio_output
                )
            
            with gr.Tab("Settings"):
                gr.Markdown("## Settings")
                model = gr.Dropdown(
                    choices=["gpt-4", "gpt-3.5-turbo", "claude-3-opus"],
                    label="AI Model",
                    value="gpt-4"
                )
                temperature = gr.Slider(
                    minimum=0.0,
                    maximum=1.0,
                    value=0.7,
                    step=0.1,
                    label="Temperature"
                )
        
        self.app = app
        return app
    
    def launch(self, share=False, server_port=None):
        """
        Launch the Gradio interface.
        
        Args:
            share: Whether to create a public link
            server_port: Port to run the server on
            
        Returns:
            Gradio app instance
        """
        if self.app is None:
            self.build_interface()
        
        server_port = server_port or int(os.getenv("GRADIO_PORT", 7860))
        logger.info(f"Launching Gradio interface on port {server_port}")
        self.app.launch(share=share, server_port=server_port)
        return self.app

def create_ui(config=None):
    """
    Create and return a configured UI instance.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        BatmanAlfredUI instance
    """
    ui = BatmanAlfredUI(config)
    return ui

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Create and launch UI
    ui = create_ui()
    ui.launch()
