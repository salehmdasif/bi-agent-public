/**
 * MessageBubble component.
 *
 * Renders a single chat message (user or assistant).
 * Assistant messages support:
 *   - Markdown rendering with react-markdown + remark-gfm
 *   - Inline Plotly chart rendering when chart_data is present
 *   - HITL approval card when pending_action is present
 *   - Tool call indicator showing which data sources were queried
 *
 * Note:
 *   Component implementation is proprietary and not included in this public version.
 */

interface MessageBubbleProps {
  role: "user" | "assistant";
  content: string;
  chartData?: object | null;
  pendingAction?: object | null;
  usedTools?: string[];
}

export default function MessageBubble(props: MessageBubbleProps) {
  throw new Error("Proprietary implementation — not included in public version");
}
