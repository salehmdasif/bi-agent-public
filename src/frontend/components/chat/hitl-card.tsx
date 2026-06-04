/**
 * HITLCard component — Human-in-the-Loop approval card.
 *
 * Renders the approval prompt for a pending agent action.
 * Shows the proposed action, a description, and Approve/Reject buttons.
 * On approval: calls POST /api/v1/chat/approve/{action_id}
 * On rejection: calls POST /api/v1/chat/reject/{action_id}
 *
 * Note:
 *   Component implementation is proprietary and not included in this public version.
 */

interface HITLCardProps {
  actionId: string;
  actionType: string;
  agentSuggestion: string;
  expiresAt: string;
  onResolved: () => void;
}

export default function HITLCard(props: HITLCardProps) {
  throw new Error("Proprietary implementation — not included in public version");
}
