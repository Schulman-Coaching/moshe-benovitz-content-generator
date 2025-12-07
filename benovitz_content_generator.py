#!/usr/bin/env python3
"""
Rabbi Moshe Benovitz Content Generator

A tool to generate content in the distinctive voice and style of Rabbi Moshe Benovitz,
NCSY International Managing Director and longtime NCSY Kollel Director.

His approach blends Torah wisdom with relatable real-world examples,
focusing on authentic growth, teen engagement, and meaningful religious development.

Author: Built with Claude
"""

import argparse
import os
import sys
from enum import Enum
from dataclasses import dataclass
from typing import Optional

try:
    import anthropic
except ImportError:
    anthropic = None


class ContentFormat(Enum):
    ARTICLE = "article"
    SOCIAL_MEDIA = "social_media"
    SHIUR_OUTLINE = "shiur_outline"
    SHORT_REFLECTION = "short_reflection"
    ADVISOR_TRAINING = "advisor_training"


@dataclass
class BenovitzVoiceProfile:
    """
    Captures the distinctive voice and style characteristics of Rabbi Moshe Benovitz.
    Based on analysis of his lectures, articles, podcast appearances, and NCSY work.
    """

    # Core characteristics
    name: str = "Rabbi Moshe Benovitz"

    # Tone attributes
    tone: str = """
    - Warm, approachable, and genuinely caring
    - Intellectually rigorous but accessible
    - Uses humor and storytelling to illustrate points
    - Direct and honest, even about difficult topics
    - Encouraging without being preachy
    - Speaks as a mentor and friend, not just authority figure
    - Balances idealism with practical realism
    """

    # Writing style patterns
    style_patterns: str = """
    - Uses relatable pop culture and sports analogies (baseball, contemporary examples)
    - Asks thought-provoking questions that challenge assumptions
    - Distinguishes between surface-level and deep transformation
    - Emphasizes authenticity over performance
    - Shares personal anecdotes and real experiences with teens
    - Builds arguments logically while remaining conversational
    - Acknowledges complexity rather than offering simplistic answers
    - Uses phrases like "What more can we do?" to inspire action
    - Balances Torah sources with practical application
    """

    # Thematic focus areas
    themes: str = """
    - Authentic religious growth vs. superficial behavior change
    - The difference between behavior modification and personality development
    - Making Halacha beloved rather than burdensome
    - Long-term mentorship and lasting relationships with students
    - Teen empowerment and seeing potential in every individual
    - Faith and doubt as part of the journey
    - The value of Torah learning as transformative experience
    - "What more can we do?" - pushing creative limits in education
    - Companionship in the educational journey
    - Making davening/tefillah inspiring and meaningful
    - The importance of genuine internal commitment over external observance
    """

    # Key influences and contexts
    influences: str = """
    - NCSY and Jewish youth outreach (kiruv)
    - Modern Orthodox education and day schools
    - Experiential education and summer programming
    - YU/Yeshiva University tradition
    - Long-term relationship-based mentorship
    - Torah learning as central transformative experience
    - Real-world application of Jewish values
    """

    # Hebrew/Jewish vocabulary commonly used
    hebrew_vocabulary: str = """
    - Kiruv (outreach/bringing close)
    - Halacha (Jewish law)
    - Davening/Tefillah (prayer)
    - Talmud Torah (Torah study)
    - Middos (character traits)
    - Machshava (Jewish thought/philosophy)
    - Teshuva (repentance/return)
    - Emunah (faith)
    - Kollel (advanced Torah study program)
    - Shiur (Torah lecture/class)
    """

    # Sentence starters and transitions commonly used
    transitions: str = """
    - "What more can we do?"
    - "Here's the thing..."
    - "The question we need to ask is..."
    - "Think about it this way..."
    - "Let me share a story..."
    - "The real challenge is..."
    - "What I've seen over 20+ years..."
    - "The difference between X and Y is..."
    - "It's not about... it's about..."
    """


def get_system_prompt(voice: BenovitzVoiceProfile) -> str:
    """Generate the system prompt for AI content generation."""

    return f"""You are a content writer who writes in the exact voice and style of {voice.name}, the Managing Director of International NCSY and longtime NCSY Kollel Director.

## VOICE PROFILE

### Tone
{voice.tone}

### Writing Style Patterns
{voice.style_patterns}

### Core Themes
{voice.themes}

### Key Influences and Context
{voice.influences}

### Hebrew/Jewish Vocabulary (use naturally, with translations where helpful)
{voice.hebrew_vocabulary}

### Common Transitions and Phrases
{voice.transitions}

## CRITICAL STYLE GUIDELINES

1. Use relatable analogies from sports, pop culture, or everyday life to illustrate Torah concepts
2. Speak as a mentor who has worked with thousands of teens over 20+ years
3. Emphasize authentic internal growth over external religious performance
4. Ask thought-provoking questions that challenge assumptions
5. Share the kind of wisdom that comes from long experience in Jewish education
6. Be honest about complexity - don't offer overly simplistic answers
7. Focus on building lasting relationships rather than quick fixes
8. Make Torah and Halacha feel meaningful and beloved, not burdensome
9. Use humor appropriately to connect and illustrate points
10. Always maintain the "what more can we do?" attitude of pushing for excellence

## CONTENT AUTHENTICITY

Write as if you ARE Rabbi Moshe Benovitz, drawing from decades of experience running NCSY Kollel, working with Jewish teens, and building the next generation of Jewish leaders. The content should feel like it comes from someone who has seen transformation happen and knows what truly works in Jewish education and kiruv."""


def get_format_instructions(format_type: ContentFormat) -> str:
    """Get specific instructions for each content format."""

    instructions = {
        ContentFormat.ARTICLE: """
## FORMAT: Long-Form Article/Essay

Structure your article as follows:

1. **Opening Hook** (1-2 paragraphs)
   - Start with a relatable story, sports analogy, or thought-provoking question
   - Connect to a universal struggle or experience

2. **The Challenge** (2-3 paragraphs)
   - Identify the real issue or misconception
   - Use your experience with teens to illustrate
   - Ask questions that make readers think

3. **Torah Perspective** (2-3 paragraphs)
   - Bring in Jewish sources naturally
   - Connect ancient wisdom to modern challenges
   - Distinguish between surface-level and deep understanding

4. **Practical Application** (2-3 paragraphs)
   - What does this mean for educators, parents, or individuals?
   - Share what you've seen work over decades of experience
   - Be realistic about the challenges while offering hope

5. **Call to Growth** (1-2 paragraphs)
   - End with encouragement and inspiration
   - Challenge readers to go deeper
   - "What more can we do?" spirit

Target length: 800-1200 words
""",

        ContentFormat.SOCIAL_MEDIA: """
## FORMAT: Social Media Post

Create an engaging social media post with:

1. **Hook** (first line) - A question, surprising insight, or relatable moment
2. **Core Message** (2-4 sentences) - The wisdom or insight
3. **Personal Touch** (1-2 sentences) - Something from your experience
4. **Reflection Point** - Question or thought to take away

Style notes:
- Use line breaks for readability
- Keep the tone warm and conversational
- Include 3-5 relevant hashtags at the end
- Appropriate for NCSY audience (teens, advisors, educators, parents)

Example hashtags: #NCSY #JewishEducation #Torah #TeenLeadership #JewishGrowth #NCSYKollel
""",

        ContentFormat.SHIUR_OUTLINE: """
## FORMAT: Shiur/Lecture Outline (NCSY Kollel Style)

Structure your shiur outline as follows:

**Title**: [Topic] - [Engaging Subtitle]

**Big Question**
- The central question or challenge this shiur addresses
- Why this matters to the audience

**Opening Hook** (5 min)
- Story, analogy, or question to grab attention
- Connect to something relatable

**Main Teaching Points** (4-6 bullet points)
- Clear, building progression of ideas
- Hebrew terms with translations
- Sources to reference (Gemara, Rambam, etc.)

**Discussion Questions** (3-4 questions)
- Questions that spark real conversation
- Challenge assumptions
- Connect to personal experience

**Real-World Application**
- How does this apply to daily life?
- What should change after this shiur?

**Takeaway**
- One powerful sentence or question to remember
""",

        ContentFormat.SHORT_REFLECTION: """
## FORMAT: Short Reflection/Daily Wisdom

Create a brief, impactful reflection:

1. **Opening Thought** (1-2 sentences)
   - An insight or observation from Jewish life/education

2. **Expansion** (2-3 sentences)
   - Brief development of the idea
   - Perhaps a quick story or example

3. **Challenge/Question** (1 sentence)
   - Leave the reader thinking

Total length: 75-150 words
Tone: Thoughtful, warm, slightly provocative
""",

        ContentFormat.ADVISOR_TRAINING: """
## FORMAT: Advisor/Educator Training Content

Create training content for NCSY advisors or Jewish educators:

**Topic**: [Training Focus]

**Why This Matters**
- Connect to the mission of reaching Jewish teens
- The real challenges advisors face

**Key Principles** (3-5 points)
- Practical guidance based on experience
- What works and what doesn't
- Common mistakes to avoid

**Scenarios**
- 2-3 realistic situations advisors might face
- How to approach each one

**The Bigger Picture**
- How this connects to genuine Jewish growth
- Remember: it's about relationships, not outcomes

**Your Challenge**
- Specific action step or mindset shift
"""
    }

    return instructions.get(format_type, instructions[ContentFormat.ARTICLE])


def generate_content_with_claude(
    topic: str,
    format_type: ContentFormat,
    api_key: Optional[str] = None,
    additional_context: str = ""
) -> str:
    """Generate content using Claude API."""

    if anthropic is None:
        return "Error: anthropic package not installed. Run: pip install anthropic"

    api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return "Error: No API key provided. Set ANTHROPIC_API_KEY environment variable or pass --api-key"

    client = anthropic.Anthropic(api_key=api_key)
    voice = BenovitzVoiceProfile()

    system_prompt = get_system_prompt(voice)
    format_instructions = get_format_instructions(format_type)

    user_prompt = f"""Please write content on the following topic:

**Topic**: {topic}

{format_instructions}

{f"**Additional Context/Notes**: {additional_context}" if additional_context else ""}

Write this content now in the authentic voice of Rabbi Moshe Benovitz."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        system=system_prompt
    )

    return message.content[0].text


def generate_content_prompt_only(
    topic: str,
    format_type: ContentFormat,
    additional_context: str = ""
) -> str:
    """Generate a complete prompt that can be used with any AI system."""

    voice = BenovitzVoiceProfile()
    system_prompt = get_system_prompt(voice)
    format_instructions = get_format_instructions(format_type)

    full_prompt = f"""=== SYSTEM INSTRUCTIONS ===
{system_prompt}

=== FORMAT INSTRUCTIONS ===
{format_instructions}

=== USER REQUEST ===
Please write content on the following topic:

**Topic**: {topic}

{f"**Additional Context/Notes**: {additional_context}" if additional_context else ""}

Write this content now in the authentic voice of Rabbi Moshe Benovitz."""

    return full_prompt


def interactive_mode():
    """Run the tool in interactive mode."""

    print("\n" + "="*60)
    print("  RABBI MOSHE BENOVITZ CONTENT GENERATOR")
    print("  NCSY Voice & Vision")
    print("="*60 + "\n")

    # Get topic
    print("What topic would you like to write about?")
    print("(Examples: 'Making tefillah meaningful', 'Authentic growth', 'Mentoring teens')")
    topic = input("\nTopic: ").strip()

    if not topic:
        print("No topic provided. Exiting.")
        return

    # Get format
    print("\nChoose a content format:")
    print("  1. Article/Essay (long-form)")
    print("  2. Social Media Post")
    print("  3. Shiur Outline (NCSY Kollel style)")
    print("  4. Short Reflection")
    print("  5. Advisor Training Content")

    format_choice = input("\nChoice (1-5): ").strip()
    format_map = {
        "1": ContentFormat.ARTICLE,
        "2": ContentFormat.SOCIAL_MEDIA,
        "3": ContentFormat.SHIUR_OUTLINE,
        "4": ContentFormat.SHORT_REFLECTION,
        "5": ContentFormat.ADVISOR_TRAINING
    }
    format_type = format_map.get(format_choice, ContentFormat.ARTICLE)

    # Get additional context
    print("\nAny additional context or notes? (Press Enter to skip)")
    additional_context = input("Context: ").strip()

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    print("\n" + "-"*60)

    if api_key:
        print("Generating content with Claude...\n")
        result = generate_content_with_claude(topic, format_type, api_key, additional_context)
        print(result)
    else:
        print("No ANTHROPIC_API_KEY found. Generating prompt template...\n")
        result = generate_content_prompt_only(topic, format_type, additional_context)
        print(result)
        print("\n" + "-"*60)
        print("Copy the above prompt and use it with Claude or another AI assistant.")

    print("\n" + "="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate content in the voice of Rabbi Moshe Benovitz",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Making tefillah meaningful for teens"
  %(prog)s "Authentic religious growth" --format social_media
  %(prog)s "The power of mentorship" --format shiur_outline
  %(prog)s --interactive
  %(prog)s --prompt-only "Building lasting relationships with students"
        """
    )

    parser.add_argument(
        "topic",
        nargs="?",
        help="The topic to write about"
    )

    parser.add_argument(
        "-f", "--format",
        choices=["article", "social_media", "shiur_outline", "short_reflection", "advisor_training"],
        default="article",
        help="Content format (default: article)"
    )

    parser.add_argument(
        "-c", "--context",
        default="",
        help="Additional context or notes for the content"
    )

    parser.add_argument(
        "--api-key",
        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)"
    )

    parser.add_argument(
        "-p", "--prompt-only",
        action="store_true",
        help="Output the prompt template instead of generating content"
    )

    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: print to stdout)"
    )

    parser.add_argument(
        "--show-voice-profile",
        action="store_true",
        help="Display the voice profile analysis"
    )

    args = parser.parse_args()

    # Show voice profile if requested
    if args.show_voice_profile:
        voice = BenovitzVoiceProfile()
        print("\n=== RABBI MOSHE BENOVITZ VOICE PROFILE ===\n")
        print(f"Name: {voice.name}")
        print(f"\nTone:{voice.tone}")
        print(f"\nStyle Patterns:{voice.style_patterns}")
        print(f"\nThemes:{voice.themes}")
        print(f"\nInfluences:{voice.influences}")
        print(f"\nHebrew Vocabulary:{voice.hebrew_vocabulary}")
        print(f"\nCommon Transitions:{voice.transitions}")
        return

    # Interactive mode
    if args.interactive:
        interactive_mode()
        return

    # Require topic if not interactive
    if not args.topic:
        parser.print_help()
        print("\nError: Please provide a topic or use --interactive mode")
        sys.exit(1)

    format_type = ContentFormat(args.format)

    # Generate content
    if args.prompt_only:
        result = generate_content_prompt_only(args.topic, format_type, args.context)
    else:
        result = generate_content_with_claude(
            args.topic,
            format_type,
            args.api_key,
            args.context
        )

    # Output
    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"Content written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
