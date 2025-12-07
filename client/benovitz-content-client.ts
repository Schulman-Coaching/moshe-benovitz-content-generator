/**
 * Rabbi Moshe Benovitz Content Generator - TypeScript Client SDK
 *
 * A client library for interacting with the Benovitz Content Generator API.
 */

export type ContentFormat = 'article' | 'social_media' | 'shiur_outline' | 'short_reflection' | 'advisor_training';

export interface GenerateRequest {
  topic: string;
  format?: ContentFormat;
  additional_context?: string;
  prompt_only?: boolean;
}

export interface GenerateResponse {
  content: string;
  format: string;
  topic: string;
}

export interface FormatInfo {
  name: string;
  value: string;
  description: string;
}

export interface VoiceProfile {
  name: string;
  tone: string;
  style_patterns: string;
  themes: string;
  influences: string;
  hebrew_vocabulary: string;
  transitions: string;
}

export interface ClientOptions {
  baseUrl?: string;
  apiKey?: string;
}

export class BenovitzContentClient {
  private baseUrl: string;
  private apiKey?: string;

  constructor(options: ClientOptions = {}) {
    this.baseUrl = options.baseUrl || 'https://benovitz-content-api.onrender.com';
    this.apiKey = options.apiKey;
  }

  private async request<T>(endpoint: string, options?: RequestInit): Promise<T> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (this.apiKey) {
      headers['Authorization'] = `Bearer ${this.apiKey}`;
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      ...options,
      headers: {
        ...headers,
        ...options?.headers,
      },
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(error.detail || `HTTP ${response.status}`);
    }

    return response.json();
  }

  /**
   * Generate content in Rabbi Benovitz's voice
   */
  async generate(request: GenerateRequest): Promise<GenerateResponse> {
    return this.request<GenerateResponse>('/generate', {
      method: 'POST',
      body: JSON.stringify({
        topic: request.topic,
        format: request.format || 'article',
        additional_context: request.additional_context || '',
        prompt_only: request.prompt_only || false,
      }),
    });
  }

  /**
   * Generate an article
   */
  async generateArticle(topic: string, context?: string): Promise<string> {
    const response = await this.generate({ topic, format: 'article', additional_context: context });
    return response.content;
  }

  /**
   * Generate a social media post
   */
  async generateSocialPost(topic: string, context?: string): Promise<string> {
    const response = await this.generate({ topic, format: 'social_media', additional_context: context });
    return response.content;
  }

  /**
   * Generate a shiur outline
   */
  async generateShiurOutline(topic: string, context?: string): Promise<string> {
    const response = await this.generate({ topic, format: 'shiur_outline', additional_context: context });
    return response.content;
  }

  /**
   * Generate a short reflection
   */
  async generateReflection(topic: string, context?: string): Promise<string> {
    const response = await this.generate({ topic, format: 'short_reflection', additional_context: context });
    return response.content;
  }

  /**
   * Generate advisor training content
   */
  async generateAdvisorTraining(topic: string, context?: string): Promise<string> {
    const response = await this.generate({ topic, format: 'advisor_training', additional_context: context });
    return response.content;
  }

  /**
   * Get available content formats
   */
  async getFormats(): Promise<FormatInfo[]> {
    const response = await this.request<{ formats: FormatInfo[] }>('/formats');
    return response.formats;
  }

  /**
   * Get the voice profile
   */
  async getVoiceProfile(): Promise<VoiceProfile> {
    return this.request<VoiceProfile>('/voice-profile');
  }

  /**
   * Get the system prompt
   */
  async getSystemPrompt(): Promise<string> {
    const response = await this.request<{ system_prompt: string }>('/system-prompt');
    return response.system_prompt;
  }

  /**
   * Health check
   */
  async healthCheck(): Promise<{ status: string; service: string }> {
    return this.request<{ status: string; service: string }>('/health');
  }
}

// React Hook
import { useState, useCallback } from 'react';

export interface UseBenovitzContentOptions {
  baseUrl?: string;
  apiKey?: string;
}

export interface UseBenovitzContentReturn {
  generate: (topic: string, format?: ContentFormat, context?: string) => Promise<void>;
  isLoading: boolean;
  error: Error | null;
  content: string | null;
  clearContent: () => void;
  clearError: () => void;
}

export function useBenovitzContent(options: UseBenovitzContentOptions = {}): UseBenovitzContentReturn {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [content, setContent] = useState<string | null>(null);

  const client = new BenovitzContentClient(options);

  const generate = useCallback(async (
    topic: string,
    format: ContentFormat = 'article',
    context?: string
  ) => {
    setIsLoading(true);
    setError(null);
    setContent(null);

    try {
      const response = await client.generate({
        topic,
        format,
        additional_context: context,
      });
      setContent(response.content);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [options.baseUrl, options.apiKey]);

  const clearContent = useCallback(() => setContent(null), []);
  const clearError = useCallback(() => setError(null), []);

  return {
    generate,
    isLoading,
    error,
    content,
    clearContent,
    clearError,
  };
}

export default BenovitzContentClient;
