"""
Base Agent Template for Specialized Agents

This module provides the base class for all specialized agents in the
Batman & Alfred Multi-Agent Framework.
"""

from typing import Dict, List, Any, Optional
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class SpecializedAgent(ABC):
    """
    Base class for all specialized agents in the framework.
    
    Specialized agents are focused on specific domains or tasks and are
    orchestrated by Alfred Prime to complete complex workflows.
    """
    
    def __init__(self, agent_id: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the specialized agent.
        
        Args:
            agent_id: Unique identifier for this agent instance
            config: Configuration dictionary for the agent
        """
        self.agent_id = agent_id
        self.config = config or {}
        self.tools = []
        self.context = {}
        logger.info(f"Specialized agent {agent_id} initialized")
    
    def register_tool(self, tool: Any) -> None:
        """
        Register a tool for the agent to use.
        
        Args:
            tool: Tool instance to be registered
        """
        self.tools.append(tool)
        logger.info(f"Tool {tool.__class__.__name__} registered with agent {self.agent_id}")
    
    @abstractmethod
    def process(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task assigned to this agent.
        
        Args:
            task: Task description and parameters
            
        Returns:
            Task results and metadata
        """
        pass
    
    def update_context(self, context_updates: Dict[str, Any]) -> None:
        """
        Update the agent's context with new information.
        
        Args:
            context_updates: Dictionary of context updates
        """
        self.context.update(context_updates)
        logger.debug(f"Updated context for agent {self.agent_id}")
