from prompts.identity import IDENTITY_PROMPT
from prompts.capabilities import CAPABILITIES_PROMPT
from prompts.tool_rules import TOOL_RULES_PROMPT
from prompts.reasoning import REASONING_PROMPT
from prompts.security import SECURITY_PROMPT
from prompts.response_style import RESPONSE_STYLE_PROMPT
from prompts.examples import EXAMPLES_PROMPT

SYSTEM_PROMPT = "\n\n".join([
    IDENTITY_PROMPT,
    CAPABILITIES_PROMPT,
    TOOL_RULES_PROMPT,
    REASONING_PROMPT,
    SECURITY_PROMPT,
    RESPONSE_STYLE_PROMPT,
    EXAMPLES_PROMPT,
])