"""
Tool Registry for External API Integrations

This module provides a registry for managing external tool integrations
in the Batman & Alfred Multi-Agent Framework.
"""

from typing import Dict, List, Any, Optional, Callable
import logging
from enum import Enum
import inspect

logger = logging.getLogger(__name__)

class ToolCategory(Enum):
    """Enum representing categories of tools."""
    DATA_RETRIEVAL = "data_retrieval"
    CONTENT_GENERATION = "content_generation"
    ANALYSIS = "analysis"
    COMMUNICATION = "communication"
    UTILITY = "utility"
    CUSTOM = "custom"

class Tool:
    """
    Represents an external tool or API integration that can be used by agents.
    """
    
    def __init__(self, 
                name: str, 
                description: str,
                function: Callable,
                category: ToolCategory = ToolCategory.UTILITY,
                parameters: Optional[Dict[str, Any]] = None,
                required_auth: bool = False):
        """
        Initialize a tool.
        
        Args:
            name: Unique name for the tool
            description: Description of what the tool does
            function: The function that implements the tool
            category: Category of the tool
            parameters: Parameter specifications for the tool
            required_auth: Whether the tool requires authentication
        """
        self.name = name
        self.description = description
        self.function = function
        self.category = category
        self.parameters = parameters or {}
        self.required_auth = required_auth
        
        # Auto-generate parameters from function signature if not provided
        if not self.parameters:
            self._extract_parameters_from_function()
        
        logger.info(f"Tool '{name}' initialized")
    
    def _extract_parameters_from_function(self):
        """Extract parameter information from the function signature."""
        sig = inspect.signature(self.function)
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
                
            param_info = {
                "type": param.annotation.__name__ if param.annotation != inspect.Parameter.empty else "any",
                "required": param.default == inspect.Parameter.empty,
            }
            
            if param.default != inspect.Parameter.empty:
                param_info["default"] = param.default
                
            self.parameters[param_name] = param_info
    
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool with the provided parameters.
        
        Args:
            **kwargs: Parameters for the tool
            
        Returns:
            Tool execution results
        """
        try:
            logger.info(f"Executing tool '{self.name}'")
            return self.function(**kwargs)
        except Exception as e:
            logger.error(f"Error executing tool '{self.name}': {e}")
            raise

class ToolRegistry:
    """
    Registry for managing and accessing tools in the framework.
    """
    
    def __init__(self):
        """Initialize the tool registry."""
        self.tools: Dict[str, Tool] = {}
        self.categories: Dict[ToolCategory, List[str]] = {category: [] for category in ToolCategory}
        logger.info("Tool registry initialized")
    
    def register_tool(self, tool: Tool) -> bool:
        """
        Register a tool with the registry.
        
        Args:
            tool: Tool instance to register
            
        Returns:
            True if registration successful, False otherwise
        """
        if tool.name in self.tools:
            logger.warning(f"Tool '{tool.name}' already registered")
            return False
        
        self.tools[tool.name] = tool
        self.categories[tool.category].append(tool.name)
        logger.info(f"Tool '{tool.name}' registered in category '{tool.category.value}'")
        return True
    
    def get_tool(self, tool_name: str) -> Optional[Tool]:
        """
        Get a tool by name.
        
        Args:
            tool_name: Name of the tool
            
        Returns:
            Tool instance if found, None otherwise
        """
        return self.tools.get(tool_name)
    
    def get_tools_by_category(self, category: ToolCategory) -> List[Tool]:
        """
        Get all tools in a specific category.
        
        Args:
            category: Tool category
            
        Returns:
            List of tools in the category
        """
        tool_names = self.categories.get(category, [])
        return [self.tools[name] for name in tool_names]
    
    def list_all_tools(self) -> List[Dict[str, Any]]:
        """
        List all registered tools with their metadata.
        
        Returns:
            List of tool information dictionaries
        """
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "category": tool.category.value,
                "parameters": tool.parameters,
                "required_auth": tool.required_auth
            }
            for tool in self.tools.values()
        ]
