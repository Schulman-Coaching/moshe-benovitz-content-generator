/**
 * Rabbi Moshe Benovitz Content Generator - JavaScript Client SDK
 *
 * A client library for interacting with the Benovitz Content Generator API.
 */

class BenovitzContentClient {
  /**
   * Create a new client instance
   * @param {Object} options - Client options
   * @param {string} [options.baseUrl] - API base URL
   * @param {string} [options.apiKey] - Optional API key
   */
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || 'https://benovitz-content-api.onrender.com';
    this.apiKey = options.apiKey;
  }

  /**
   * Make an API request
   * @private
   */
  async request(endpoint, options = {}) {
    const headers = {
      'Content-Type': 'application/json',
    };

    if (this.apiKey) {
      headers['Authorization'] = `Bearer ${this.apiKey}`;
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      ...options,
      headers: {
        ...headers,
        ...options.headers,
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
   * @param {Object} request - Generation request
   * @param {string} request.topic - The topic to write about
   * @param {string} [request.format='article'] - Content format
   * @param {string} [request.additional_context] - Additional context
   * @param {boolean} [request.prompt_only=false] - Return prompt only
   * @returns {Promise<{content: string, format: string, topic: string}>}
   */
  async generate(request) {
    return this.request('/generate', {
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
   * @param {string} topic - The topic to write about
   * @param {string} [context] - Additional context
   * @returns {Promise<string>} Generated content
   */
  async generateArticle(topic, context) {
    const response = await this.generate({ topic, format: 'article', additional_context: context });
    return response.content;
  }

  /**
   * Generate a social media post
   * @param {string} topic - The topic to write about
   * @param {string} [context] - Additional context
   * @returns {Promise<string>} Generated content
   */
  async generateSocialPost(topic, context) {
    const response = await this.generate({ topic, format: 'social_media', additional_context: context });
    return response.content;
  }

  /**
   * Generate a shiur outline
   * @param {string} topic - The topic to write about
   * @param {string} [context] - Additional context
   * @returns {Promise<string>} Generated content
   */
  async generateShiurOutline(topic, context) {
    const response = await this.generate({ topic, format: 'shiur_outline', additional_context: context });
    return response.content;
  }

  /**
   * Generate a short reflection
   * @param {string} topic - The topic to write about
   * @param {string} [context] - Additional context
   * @returns {Promise<string>} Generated content
   */
  async generateReflection(topic, context) {
    const response = await this.generate({ topic, format: 'short_reflection', additional_context: context });
    return response.content;
  }

  /**
   * Generate advisor training content
   * @param {string} topic - The topic to write about
   * @param {string} [context] - Additional context
   * @returns {Promise<string>} Generated content
   */
  async generateAdvisorTraining(topic, context) {
    const response = await this.generate({ topic, format: 'advisor_training', additional_context: context });
    return response.content;
  }

  /**
   * Get available content formats
   * @returns {Promise<Array<{name: string, value: string, description: string}>>}
   */
  async getFormats() {
    const response = await this.request('/formats');
    return response.formats;
  }

  /**
   * Get the voice profile
   * @returns {Promise<Object>} Voice profile details
   */
  async getVoiceProfile() {
    return this.request('/voice-profile');
  }

  /**
   * Get the system prompt
   * @returns {Promise<string>} System prompt
   */
  async getSystemPrompt() {
    const response = await this.request('/system-prompt');
    return response.system_prompt;
  }

  /**
   * Health check
   * @returns {Promise<{status: string, service: string}>}
   */
  async healthCheck() {
    return this.request('/health');
  }
}

// Export for different module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BenovitzContentClient;
}

if (typeof window !== 'undefined') {
  window.BenovitzContentClient = BenovitzContentClient;
}
