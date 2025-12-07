/**
 * Sample React Component for Rabbi Moshe Benovitz Content Generator
 *
 * Copy this component into your React application and customize as needed.
 */

import React, { useState } from 'react';
import { useBenovitzContent, ContentFormat } from './benovitz-content-client';

// Configuration - Production API URL on Render
const API_URL = process.env.REACT_APP_BENOVITZ_API_URL || 'https://moshe-benovitz-content-generator-api.onrender.com';

interface ContentGeneratorProps {
  className?: string;
}

export const ContentGenerator: React.FC<ContentGeneratorProps> = ({ className }) => {
  const [topic, setTopic] = useState('');
  const [format, setFormat] = useState<ContentFormat>('article');
  const [additionalContext, setAdditionalContext] = useState('');

  const {
    generate,
    isLoading,
    error,
    content,
    clearContent,
    clearError,
  } = useBenovitzContent({
    baseUrl: API_URL,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!topic.trim()) return;

    try {
      await generate(topic, format, additionalContext);
    } catch (err) {
      // Error is already captured in the hook
      console.error('Generation failed:', err);
    }
  };

  const formatOptions: { value: ContentFormat; label: string; description: string }[] = [
    { value: 'article', label: 'Article', description: 'Long-form essay (800-1200 words)' },
    { value: 'social_media', label: 'Social Media', description: 'Short post with hashtags' },
    { value: 'shiur_outline', label: 'Shiur Outline', description: 'NCSY Kollel-style lecture plan' },
    { value: 'short_reflection', label: 'Reflection', description: 'Brief daily wisdom (75-150 words)' },
    { value: 'advisor_training', label: 'Advisor Training', description: 'Training content for NCSY advisors' },
  ];

  return (
    <div className={`content-generator ${className || ''}`}>
      <h2>Generate Content in Rabbi Benovitz's Voice</h2>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="topic">Topic</label>
          <input
            id="topic"
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="e.g., Making tefillah meaningful for teens"
            disabled={isLoading}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="format">Format</label>
          <select
            id="format"
            value={format}
            onChange={(e) => setFormat(e.target.value as ContentFormat)}
            disabled={isLoading}
          >
            {formatOptions.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label} - {opt.description}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="context">Additional Context (optional)</label>
          <textarea
            id="context"
            value={additionalContext}
            onChange={(e) => setAdditionalContext(e.target.value)}
            placeholder="e.g., For NCSY summer program staff training"
            disabled={isLoading}
            rows={3}
          />
        </div>

        <button type="submit" disabled={isLoading || !topic.trim()}>
          {isLoading ? 'Generating...' : 'Generate Content'}
        </button>
      </form>

      {error && (
        <div className="error">
          <p>Error: {error.message}</p>
          <button onClick={clearError}>Dismiss</button>
        </div>
      )}

      {content && (
        <div className="content-output">
          <div className="content-header">
            <h3>Generated Content</h3>
            <button onClick={clearContent}>Clear</button>
          </div>
          <div className="content-body">
            <pre>{content}</pre>
          </div>
          <button
            onClick={() => navigator.clipboard.writeText(content)}
            className="copy-button"
          >
            Copy to Clipboard
          </button>
        </div>
      )}

      <style>{`
        .content-generator {
          max-width: 800px;
          margin: 0 auto;
          padding: 20px;
          font-family: system-ui, -apple-system, sans-serif;
        }

        .form-group {
          margin-bottom: 16px;
        }

        .form-group label {
          display: block;
          margin-bottom: 4px;
          font-weight: 600;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
          width: 100%;
          padding: 8px 12px;
          border: 1px solid #ccc;
          border-radius: 4px;
          font-size: 16px;
        }

        .form-group textarea {
          resize: vertical;
        }

        button {
          padding: 10px 20px;
          background: #1a365d;
          color: white;
          border: none;
          border-radius: 4px;
          font-size: 16px;
          cursor: pointer;
        }

        button:hover:not(:disabled) {
          background: #2c5282;
        }

        button:disabled {
          background: #9ca3af;
          cursor: not-allowed;
        }

        .error {
          margin-top: 16px;
          padding: 12px;
          background: #fee2e2;
          border: 1px solid #ef4444;
          border-radius: 4px;
          color: #dc2626;
        }

        .error button {
          background: #ef4444;
          margin-top: 8px;
        }

        .content-output {
          margin-top: 24px;
          border: 1px solid #e5e7eb;
          border-radius: 8px;
          overflow: hidden;
        }

        .content-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 12px 16px;
          background: #f9fafb;
          border-bottom: 1px solid #e5e7eb;
        }

        .content-header h3 {
          margin: 0;
        }

        .content-header button {
          padding: 6px 12px;
          background: #6b7280;
          font-size: 14px;
        }

        .content-body {
          padding: 16px;
          max-height: 500px;
          overflow-y: auto;
        }

        .content-body pre {
          margin: 0;
          white-space: pre-wrap;
          word-wrap: break-word;
          font-family: inherit;
          line-height: 1.6;
        }

        .copy-button {
          display: block;
          width: 100%;
          border-radius: 0;
          background: #059669;
        }

        .copy-button:hover {
          background: #047857;
        }
      `}</style>
    </div>
  );
};

export default ContentGenerator;
