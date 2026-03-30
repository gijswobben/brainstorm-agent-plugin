# Advanced Brainstorming Agent Plugin

This plugin is designed to enhance the brainstorming and idea generation process by providing advanced features and tools. It allows users to generate creative ideas, organize them effectively, and collaborate with others in a seamless manner.

## Whats in the box?

### Agents

- **Virtual Brainstormer**: A specialist in planning and facilitating virtual brainstorm sessions for AI agents. It works with the user to shape a clear, practical session plan before anything starts. The plan is executed by AI agents, not humans, and therefore the plan is to the point and precise. When the plan is ready, it converts it into a task list and hands it off to the appropriate agent to execute the brainstorm session.

### Sub-Agents (not for direct use, but can be used by the Virtual Brainstormer)

- **Chain Method Brainstormer**: Expert in using the Chain Method brainstorming technique to generate creative ideas and solutions by connecting random words to a specific problem or challenge. This method is great for breaking out of usual thought patterns and generating creative solutions. You can tell this agent to do a specific number of rounds of the Chain Method (more rounds means more ideas, the default number of rounds is 10), and it will return the generated ideas in a structured format.
- **Superhero Method Brainstormer**: Expert in using the Superhero Method brainstorming technique to generate creative ideas and solutions by imagining how a superhero or other character would solve a specific problem or challenge. This method is great for thinking outside the box and generating unique solutions. You can tell this agent to do a specific number of rounds of the Superhero Method (more rounds means more ideas, the default number of rounds is 10), and it will return the generated ideas in a structured format.

### Skills

- **/random**: A skill that generates random words or phrases, which can be used in brainstorming sessions to spark creativity and generate new ideas.
- **/feasibility-check**: A skill that evaluates the feasibility of an idea, project, or solution based on various factors such as resources, time, cost, and potential obstacles.


## Installation

### GitHub Copilot CLI
To install the Advanced Brainstorming Agent Plugin, run the following command in your terminal (GitHub Copilot CLI must be installed and configured):

```bash
copilot plugin install https://github.com/gijswobben/brainstorm-agent-plugin
```

### VS Code Extension
To install the Advanced Brainstorming Agent Plugin as a VS Code extension, follow these steps:

1. Run _"Chat: Install Plugin From Source"_ from the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
2. Enter the URL of the plugin repository: `https://github.com/gijswobben/brainstorm-agent-plugin`
