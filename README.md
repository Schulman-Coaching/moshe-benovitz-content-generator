# Rabbi Moshe Benovitz Content Generator

AI-powered content generator in Rabbi Moshe Benovitz's distinctive voice — blending relatable wisdom, authentic religious growth, and NCSY's transformative approach to Jewish education.

## Features

- **Voice Profile**: Based on analysis of Rabbi Benovitz's lectures, articles, and NCSY leadership
- **Multiple Formats**: Articles, social media posts, shiur outlines, reflections, and advisor training
- **Flexible Integration**: CLI tool, REST API, or direct Python embedding
- **AI-Powered**: Uses Claude for intelligent content generation

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### CLI Usage

```bash
# Interactive mode
python benovitz_content_generator.py --interactive

# Generate an article
python benovitz_content_generator.py "Making tefillah meaningful" --format article

# Generate a social media post
python benovitz_content_generator.py "Authentic religious growth" --format social_media

# Generate a shiur outline
python benovitz_content_generator.py "The power of mentorship" --format shiur_outline

# Generate advisor training content
python benovitz_content_generator.py "Building relationships with teens" --format advisor_training

# Get just the prompt (no API key needed)
python benovitz_content_generator.py --prompt-only "Teen empowerment"

# View the voice profile
python benovitz_content_generator.py --show-voice-profile
```

### Environment Setup

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Live API

The API is deployed and available at:

**Production URL**: `https://benovitz-content-api.onrender.com`

**Interactive Docs**: https://benovitz-content-api.onrender.com/docs

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate` | POST | Generate content |
| `/formats` | GET | List available formats |
| `/voice-profile` | GET | Get voice profile |
| `/system-prompt` | GET | Get the full system prompt |
| `/health` | GET | Health check |
| `/docs` | GET | Interactive API documentation |

### Example API Request

```bash
# Generate a shiur outline
curl -X POST "https://benovitz-content-api.onrender.com/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Making davening meaningful for teens",
    "format": "shiur_outline"
  }'

# Generate a social media post
curl -X POST "https://benovitz-content-api.onrender.com/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "What more can we do?",
    "format": "social_media"
  }'
```

### JavaScript/React Integration

```javascript
// Using the provided client SDK
import BenovitzContentClient from './client/benovitz-content-client';

const client = new BenovitzContentClient('https://benovitz-content-api.onrender.com');

// Generate content
const article = await client.generateArticle('Authentic religious growth');
const socialPost = await client.generateSocialPost('Teen leadership');
const shiurOutline = await client.generateShiurOutline('Making Halacha beloved');
const reflection = await client.generateReflection('Mentorship');
const training = await client.generateAdvisorTraining('Building relationships');
```

### React Hook Usage

```javascript
import { useBenovitzContent } from './client/benovitz-content-client';

function ContentGenerator() {
  const { generate, isLoading, error, content } = useBenovitzContent({
    baseUrl: 'https://benovitz-content-api.onrender.com'
  });

  const handleGenerate = async () => {
    await generate('Making tefillah meaningful', 'article');
  };

  return (
    <div>
      <button onClick={handleGenerate} disabled={isLoading}>
        {isLoading ? 'Generating...' : 'Generate'}
      </button>
      {content && <pre>{content}</pre>}
    </div>
  );
}
```

## Content Formats

### 1. Article/Essay
Long-form content (800-1200 words) with:
- Opening hook with relatable story or analogy
- The challenge or misconception
- Torah perspective and sources
- Practical application
- Call to growth

### 2. Social Media
Short-form posts with:
- Compelling hook
- Core wisdom (2-4 sentences)
- Personal touch from experience
- Reflection point
- NCSY-relevant hashtags

### 3. Shiur Outline (NCSY Kollel Style)
Lecture plans with:
- Big question to address
- Opening hook
- Main teaching points with sources
- Discussion questions
- Real-world application
- Takeaway

### 4. Short Reflection
Brief daily wisdom (75-150 words):
- Opening thought
- Brief expansion
- Challenge or question

### 5. Advisor Training
Training content for educators with:
- Why this matters for reaching teens
- Key principles from experience
- Realistic scenarios
- The bigger picture
- Actionable challenge

## Voice Profile

The generator captures Rabbi Moshe Benovitz's distinctive voice:

**Tone**
- Warm, approachable, and genuinely caring
- Intellectually rigorous but accessible
- Uses humor and storytelling
- Direct and honest about difficult topics
- Encouraging without being preachy

**Style Patterns**
- Relatable pop culture and sports analogies
- Thought-provoking questions
- Distinguishes surface-level from deep transformation
- Emphasizes authenticity over performance
- Personal anecdotes from 20+ years with teens

**Key Themes**
- Authentic growth vs. superficial behavior change
- "What more can we do?" philosophy
- Making Halacha beloved, not burdensome
- Long-term mentorship and relationships
- Torah learning as transformative experience

**Key Influences**
- NCSY and Jewish youth outreach
- Modern Orthodox education
- Experiential and summer programming
- YU/Yeshiva University tradition
- Relationship-based mentorship

## Deployment

### Current Production (Render)

The API is deployed on Render at `https://benovitz-content-api.onrender.com`

To deploy your own instance:

1. Fork this repository
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Set environment variable: `ANTHROPIC_API_KEY`
5. Render will auto-detect settings from `render.yaml`

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY="your-key"

# Run the server
uvicorn api:app --reload --port 8000
```

## Integration with NCSY Platforms

This API is designed to integrate with:
- **NCSY websites** - Content generation
- **NCSY Kollel** - Shiur outlines and materials
- **Advisor training** - Educational content
- **Social media** - Scheduled posts
- **Email newsletters** - Weekly wisdom

## License

MIT License - See LICENSE file for details.

## Credits

Built with Claude by Schulman Coaching.

Voice profile based on analysis of Rabbi Moshe Benovitz's work as:
- NCSY International Managing Director
- NCSY Kollel Director (20+ years)
- Jewish educator and speaker
