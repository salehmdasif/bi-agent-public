/**
 * API client for the BI Agent Platform backend.
 *
 * Wraps fetch with auth token injection, error handling, and
 * token refresh on 401 responses.
 *
 * Note:
 *   API client implementation is proprietary and not included in this public version.
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function apiPost<T>(path: string, body: unknown): Promise<T> {
  /**
   * Make an authenticated POST request.
   *
   * Injects the current access token from local storage.
   * On 401: attempts token refresh and retries once.
   *
   * Note:
   *   Implementation is proprietary and not included in this public version.
   */
  throw new Error("Proprietary implementation — not included in public version");
}

export async function apiGet<T>(path: string): Promise<T> {
  /**
   * Make an authenticated GET request.
   *
   * Note:
   *   Implementation is proprietary and not included in this public version.
   */
  throw new Error("Proprietary implementation — not included in public version");
}

export async function apiDelete(path: string): Promise<void> {
  /**
   * Make an authenticated DELETE request.
   *
   * Note:
   *   Implementation is proprietary and not included in this public version.
   */
  throw new Error("Proprietary implementation — not included in public version");
}
