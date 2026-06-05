from mcp.server.fastmcp import FastMCP

from tools.status import swm_status_tool
from tools.discover import swm_discover_context_tool, swm_write_discovery_tool
from tools.extract import swm_extract_context_tool, swm_write_extract_tool

mcp = FastMCP("SpecWingman")


@mcp.tool()
def swm_status(project_path: str) -> str:
    """Scan specs/ directory and return SpecWingman workflow progress."""
    return swm_status_tool(project_path)


@mcp.tool()
def swm_discover_context(project_path: str) -> str:
    """Step 1 (Discovery): Return the assembled prompt, CONSTITUTION, and all input files for the calling AI to process. After processing, call swm_write_discovery with the results."""
    return swm_discover_context_tool(project_path)


@mcp.tool()
def swm_write_discovery(
    project_path: str,
    source_summary: str,
    extracted_facts: str,
    open_questions: str,
    assumptions: str,
    glossary: str,
) -> str:
    """Step 1 (Discovery): Write the AI-generated discovery files to specs/01-discovery/."""
    return swm_write_discovery_tool(
        project_path, source_summary, extracted_facts, open_questions, assumptions, glossary
    )


@mcp.tool()
def swm_extract_context(project_path: str) -> str:
    """Step 2 (Requirements): Return the assembled prompt, CONSTITUTION, and discovery files for the calling AI to process. After processing, call swm_write_extract with the results."""
    return swm_extract_context_tool(project_path)


@mcp.tool()
def swm_write_extract(
    project_path: str,
    product_vision: str,
    functional_requirements: str,
    business_rules: str,
    data_requirements: str,
    workflow_requirements: str,
    permission_requirements: str,
    non_functional_requirements: str,
    user_roles: str,
) -> str:
    """Step 2 (Requirements): Write the AI-generated requirements files to specs/02-requirements/."""
    return swm_write_extract_tool(
        project_path,
        product_vision,
        functional_requirements,
        business_rules,
        data_requirements,
        workflow_requirements,
        permission_requirements,
        non_functional_requirements,
        user_roles,
    )


if __name__ == "__main__":
    mcp.run()
