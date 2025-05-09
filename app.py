import asyncio
from fastmcp import FastMCP, Client

# Create a FastMCP server instance
mcp = FastMCP("Demo")

# Define a simple tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

async def main():
    # Connect to the server via in-memory transport
    async with Client(mcp) as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)
        # Call the 'add' tool and get the first response
        responses = await client.call_tool("add", {"a": 7, "b": 5})
        # call_tool returns a list of responses
        result = responses[0]
        print("7 + 5 =", result.text)

if __name__ == "__main__":
    # Run the demo
    asyncio.run(main())